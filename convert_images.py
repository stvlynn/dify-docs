import os
import re
import hashlib
from PIL import Image
import boto3
from botocore.client import Config
import requests
from pathlib import Path
import io
import yaml
from tqdm import tqdm
import time
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('image_conversion.log'),
        logging.StreamHandler()
    ]
)

# S3配置
S3_ENDPOINT = 'https://305dbc7da819eb47bb3f3f3bc8927046.r2.cloudflarestorage.com'
S3_ACCESS_KEY = 'cab6da8bc1afc482c908870a079dc995'
S3_SECRET_KEY = '9dd9cfc5e24bc207c42994d494bde5212b832b821690812f07b3d4f0c665639a'
S3_BUCKET = 'assets-doc'
CDN_DOMAIN = 'https://assets-docs.dify.ai'

# 进度文件路径
PROGRESS_FILE = 'conversion_progress.yaml'

# 创建S3客户端
s3_client = boto3.client(
    's3',
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

def load_progress():
    """加载进度信息"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    return {}

def save_progress(progress):
    """保存进度信息"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(progress, f)

def convert_to_webp(image_path):
    """将图片转换为WebP格式"""
    try:
        # 跳过远程图片
        if image_path.startswith(('http://', 'https://')):
            logging.info(f"跳过远程图片: {image_path}")
            return None

        img = Image.open(image_path)
        
        # 转换为RGB模式（如果是RGBA，保持RGBA）
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGB')
        
        # 创建一个字节流对象
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='WEBP', quality=80)
        img_byte_arr.seek(0)
        
        return img_byte_arr
    except Exception as e:
        logging.error(f"转换图片失败: {image_path}, 错误: {str(e)}")
        return None

def get_md5(content):
    """获取内容的MD5值"""
    if isinstance(content, io.BytesIO):
        return hashlib.md5(content.getvalue()).hexdigest()
    return hashlib.md5(content).hexdigest()

def upload_to_s3(img_data, lang_folder, subfolder=''):
    """上传图片到S3"""
    try:
        md5_name = get_md5(img_data) + '.webp'
        s3_path = f'img/{lang_folder}/{subfolder}/{md5_name}'.replace('//', '/')
        
        img_data.seek(0)
        s3_client.upload_fileobj(
            img_data,
            S3_BUCKET,
            s3_path,
            ExtraArgs={'ContentType': 'image/webp'}
        )
        
        return f'{CDN_DOMAIN}/{s3_path}'
    except Exception as e:
        logging.error(f"上传到S3失败: {str(e)}")
        return None

def process_markdown_file(file_path, lang, progress):
    """处理单个Markdown文件"""
    file_key = os.path.relpath(file_path, os.path.dirname(os.path.dirname(file_path)))
    
    # 检查是否已处理
    if file_key in progress:
        logging.info(f"跳过已处理的文件: {file_key}")
        return True

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        original_content = content

        # 查找Markdown中的图片链接
        img_pattern = r'!\[.*?\]\((.*?)\)'
        matches = re.finditer(img_pattern, content)
        modified = False
        success = True

        for match in matches:
            img_path = match.group(1)
            if img_path.startswith(CDN_DOMAIN):  # 跳过已经处理过的图片
                continue
            
            # 如果是远程图片，跳过处理
            if img_path.startswith(('http://', 'https://')):
                continue

            # 获取相对路径作为S3子文件夹
            relative_path = os.path.dirname(os.path.relpath(file_path, os.path.join(os.path.dirname(file_path), '..')))
            
            # 转换为绝对路径
            absolute_img_path = os.path.abspath(os.path.join(os.path.dirname(file_path), img_path))
            
            # 转换图片为WebP
            img_data = convert_to_webp(absolute_img_path)
            if img_data:
                # 上传到S3
                s3_url = upload_to_s3(img_data, lang, relative_path)
                if s3_url:
                    # 替换原文件中的图片链接
                    content = content.replace(match.group(1), s3_url)
                    modified = True
                else:
                    success = False
                    break
            else:
                success = False
                break

        # 只有在所有操作都成功时才写入文件
        if modified and success:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            progress[file_key] = {
                'processed_time': time.time(),
                'status': 'success'
            }
            save_progress(progress)
            logging.info(f"已处理文件: {file_key}")
            return True
        elif not success:
            logging.warning(f"处理失败，保持原文件不变: {file_key}")
            return False
        else:
            progress[file_key] = {
                'processed_time': time.time(),
                'status': 'no_changes_needed'
            }
            save_progress(progress)
            logging.info(f"文件无需修改: {file_key}")
            return True

    except Exception as e:
        logging.error(f"处理文件失败: {file_path}, 错误: {str(e)}")
        return False

def get_markdown_files(directory):
    """获取目录下所有的Markdown文件"""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def process_directory(directory, lang):
    """处理目录下的所有Markdown文件"""
    progress = load_progress()
    markdown_files = get_markdown_files(directory)
    
    with tqdm(total=len(markdown_files), desc=f"处理{lang}文档") as pbar:
        for file_path in markdown_files:
            process_markdown_file(file_path, lang, progress)
            pbar.update(1)

def main():
    # 处理中文、英文、日文文档
    base_dir = os.path.dirname(os.path.abspath(__file__))
    directories = {
        'zh_CN': os.path.join(base_dir, 'zh_CN'),
        'en': os.path.join(base_dir, 'en'),
        'jp': os.path.join(base_dir, 'jp')
    }

    for lang, directory in directories.items():
        logging.info(f"开始处理{lang}文档...")
        process_directory(directory, lang)
        logging.info(f"完成处理{lang}文档")

if __name__ == '__main__':
    main()
