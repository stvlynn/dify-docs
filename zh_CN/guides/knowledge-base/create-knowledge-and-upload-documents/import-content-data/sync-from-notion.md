# 1.1 从 Notion 导入数据

Dify 知识库支持从 Notion 导入，并支持后续的数据自动同步。

### 授权验证

1. 在创建知识库，选择数据源时，点击 **同步自 Notion 内容-- 去绑定，根据提示完成授权验证。**
2. 你也可以：进入 **设置 -- 数据来源 -- 添加数据源** 中点击 Notion 来源 **绑定** ，完成授权验证。

<figure><img src="https://assets-docs.dify.ai/2024/12/f1d5bcdcfbd57407e0bce1597df4daad.png" alt=""><figcaption><p>绑定 Notion</p></figcaption></figure>

### 导入 Notion 数据

完成验证授权后，进入创建知识库页面，点击**同步自 Notion 内容**，选择需要的授权页面进行导入。

![Import from notion](https://assets-docs.dify.ai/2025/01/ac130faeb40a59662c2f63b9680d061e.png)

### 进行分段和清洗

接下来，选择知识库的**分段设置**和**索引方式**，**保存并处理**。等待 Dify 自动处理数据。Dify 不仅可以导入 Notion 的普通类型页面，同时也支持导入并汇总保存 database 类型下的页面属性。

_**请注意：暂不支持导入图片和文件，表格类数据会被转换为文本展示。**_

![预览 Notion 页的分段结果](https://assets-docs.dify.ai/2024/12/ab1b1aa690adad153cac0a321b6b7585.png)

### 同步 Notion 数据

如果你的 Notion 内容有更新，可以在知识库的 **文档列表页**中点击对应内容页的 **同步** 按钮进行数据同步。同步文档涉及嵌入过程，因此将消耗嵌入模型的 Tokens。

<figure><img src="https://assets-docs.dify.ai/2024/12/af7cabd98c3aac392819d9041cc408de.png" alt=""><figcaption><p>同步 Notion 内容</p></figcaption></figure>

### 社区版 Notion 的集成配置方法

Notion 分为**内部集成**（internal integration）和**外部集成**（public integration）两种方式，两种集成方式的具体区别请参阅 [Notion 官方文档](https://developers.notion.com/docs/authorization)。

### 1、**使用 internal 集成方式**

首先，在集成的设置页面中[创建集成](https://www.notion.so/my-integrations)。默认情况下，所有集成都以内部集成开始；内部集成将与你选择的工作区相关联，因此你需要是工作区所有者才能创建集成。

具体操作步骤：

点击“**New integration**”按钮，类型默认是 **Internal**（不可修改），选择关联的空间，输入集成名称并上传 logo 后，点击“Submit”，集成创建成功。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/import-content-data/a560c828fea533e89ad7338ec32d5cb3.webp" alt=""><figcaption></figcaption></figure>

创建集成后，你可以根据需要在 Capabilities 选项卡下更新其设置，并在 Secrets 下点击 “Show” 按钮然后复制 Secrets。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/import-content-data/47e9610ca2036a0569a3e1e9a7a7eb5d.webp" alt=""><figcaption></figcaption></figure>

复制后回到 Dify 源代码下，在 **.env** 文件里配置相关环境变量，环境变量如下：

```
NOTION_INTEGRATION_TYPE = internal or NOTION_INTEGRATION_TYPE = public
NOTION_INTERNAL_SECRET=you-internal-secret
```

### 2、**使用 Public 集成方式**

**需要将 internal 集成升级为 public 集成**，导航到集成的 Distribution 页面，然后切换开关以公开集成。将开关切换到公共设置，你需要在下面的 Organization Information 表单中填写其他信息，包括你的公司名称、网站和重定向 URL 等信息，然后点击“Submit”按钮。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/import-content-data/65818ad8198396626d23791397ede90e.webp" alt=""><figcaption></figcaption></figure>

在集成的设置页面中成功公开集成后，你将能够在密钥选项卡中访问集成的密钥：

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/import-content-data/b7aacbaddbfb61ca799ac37557444422.webp" alt="" width="375"><figcaption></figcaption></figure>

回到 Dify 源代码下，在 **.env** 文件里配置相关环境变量，环境变量如下：

```
NOTION_INTEGRATION_TYPE=public
NOTION_CLIENT_SECRET=you-client-secret
NOTION_CLIENT_ID=you-client-id
```

配置完成后，即可在知识库中操作 Notion 的数据导入及同步功能。
