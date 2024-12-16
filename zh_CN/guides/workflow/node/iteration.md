# 迭代

### 定义

对数组中的元素依次执行相同的操作步骤，直至输出所有结果，可以理解为任务批处理器。迭代节点通常配合数组变量使用。

例如在长文翻译迭代节点内，如果将所有内容输入至 LLM 节点，有可能会达到单次对话限制。上游节点可以先将长文拆分为了多个片段，配合迭代节点对各个片段执行批量翻译，以避免达到 LLM 单次对话的消息限制。

***

### 功能简介

使用迭代的条件是确保输入值已格式化为列表对象；迭代节点将依次处理迭代开始节点数组变量内的所有元素，每个元素遵循相同的处理步骤，每轮处理被称为一个迭代，最终输出处理结果。

迭代节点的结构通常包含**输入变量**、**迭代工作流**、**输出变量**三个功能单元。

**输入变量：**&#x4EC5;接受 Array 数组变量类型数据。如果你不了解什么是数组变量，请阅读 [扩展阅读：数组](../../../learn-more/extended-reading/what-is-array-variable.md)。

**迭代工作流：**&#x4F60;可以在迭代节点中使用多个工作流节点，编排不同的任务步骤。

**输出变量：**&#x4EC5;支持输出数组变量 `Array[List]`。如果你想要输出其它变量格式，请阅读 [扩展阅读：如何将数组转换为文本](iteration.md#ru-he-jiang-shu-zu-zhuan-huan-wei-wen-ben)。

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/165f0fedb99a51e1f83a70bd0e991e45.webp" alt=""><figcaption><p>迭代节点原理图</p></figcaption></figure>

### 场景

#### **示例1：长文章迭代生成器**

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/f0d31ff3a11a2b270755053e3a95c8a4.webp" alt=""><figcaption><p>长故事生成器</p></figcaption></figure>

1. 在 **开始节点** 内添加输入故事标题、大纲变量，提示用户手动输入初始信息
2. 使用 **LLM 节点**基于用户输入的故事标题和大纲，让 LLM 开始编写内容
3. 使用 **参数提取节点** 将 LLM 输出的完整内容转换成数组格式
4. 通过 **迭代节点** 包裹的 **LLM 节点** 循环多次生成各章节内容
5. 将 **直接回复** 节点添加在迭代节点内部，实现在每轮迭代生成之后流式输出

**具体配置步骤**

1. 在 **开始节点** 配置故事标题（title）和大纲（outline）；

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/d806da73a4399dc724f295ec5490b2e3.webp" alt="" width="375"><figcaption><p>开始节点配置</p></figcaption></figure>

2. 选择 **LLM 节点** 基于用户输入的故事标题和大纲，让 LLM 开始编写文本；

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/40880c6c0b5053055b189304889dd7ad.webp" alt="" width="375"><figcaption><p>模板节点</p></figcaption></figure>

3. 选择 **参数提取节点**，将故事文本转换成为数组（Array）结构。提取参数为 `sections` ，参数类型为 `Array[Object]`

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/eed37dc5b530cdf8161ab73b2e9c44ea.webp" alt="" width="375"><figcaption><p>参数提取</p></figcaption></figure>

{% hint style="info" %}
参数提取效果受模型推理能力和指令影响，使用推理能力更强的模型，在**指令**内增加示例可以提高参数提取的效果。
{% endhint %}

4. 将数组格式的故事大纲作为迭代节点的输入，在迭代节点内部使用 **LLM 节点** 进行处理

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/cb4e182a13838875c81dafdcc238e6eb.webp" alt="" width="375"><figcaption><p>配置迭代节点</p></figcaption></figure>

在 LLM 节点内配置输入变量 `GenerateOverallOutline/output` 和 `Iteration/item`

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/dcae309a8382cfe32ceb977395077327.webp" alt="" width="375"><figcaption><p>配置 LLM 节点</p></figcaption></figure>

{% hint style="info" %}
迭代的内置变量：`items[object]` 和 `index[number]`

`items[object] 代表以每轮迭代的输入条目；`

`index[number] 代表当前迭代的轮次；`
{% endhint %}

5. 在迭代节点内部配置 **直接回复节点** ，可以实现在每轮迭代生成之后流式输出。

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/eccbd8e2ae58516211c474cebde9ed70.webp" alt="" width="375"><figcaption><p>配置 Answer 节点</p></figcaption></figure>

6. 完整调试和预览

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/549a618aa01e6a2e27267708ef65d09e.webp" alt=""><figcaption><p>按故事章节多轮迭代生成</p></figcaption></figure>

#### **示例 2：长文章迭代生成器（另一种编排方式）**

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/a8ee9d1193ce5142259066b6f2f3f885.webp" alt=""><figcaption></figcaption></figure>

* 在 **开始节点** 内输入故事标题和大纲
* 使用 **LLM 节点** 生成文章小标题，以及小标题对应的内容
* 使用 **代码节点** 将完整内容转换成数组格式
* 通过 **迭代节点** 包裹的 **LLM 节点** 循环多次生成各章节内容
* 使用 **模板转换** 节点将迭代节点输出的字符串数组转换为字符串
* 在最后添加 **直接回复节点** 将转换后的字符串直接输出

***

### 高级功能

**并行模式**

迭代节点支持并行模式，开启后将有效提升迭代节点的整体运行效率。

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/138c1cbd597a44692082410377021710.webp" alt=""><figcaption></figcaption></figure>

下图是迭代节点开启或关闭并行模式的运行效果对比。

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/ceb872bf59de4045fce1be3f68e7cbe9.webp" alt=""><figcaption><p>顺序与并行执行原理图</p></figcaption></figure>

并行模式下的最高并行轮数为 10，这意味着单位时间内最多可以同时运行 10 个任务。如果需要处理超过  10 个任务，前 10 个元素将率先同时运行，前排任务处理完成后将继续处理剩余任务。

{% hint style="info" %}
开启并行模式后，不再建议在迭代节点内放置直接回答、变量赋值和工具节点。此举可能会造成异常情况。
{% endhint %}

* **错误响应方法**

迭代节点通常需要处理大量任务，有时会在处理某个元素时发生错误。为了避免某个元素异常而中断所有任务，你可以在**错误响应方法**中设置异常的应对方法：

* 错误时终止。如果发现异常输出，终止迭代节点，输出错误信息。
* 忽略错误并继续。忽略异常信息，继续处理剩余元素。输出的信息中包含正确信息，异常信息为空值。
* 移除错误输出。忽略异常信息，继续处理剩余元素。输出的信息中仅包含正确信息。

迭代节点的输入变量与输出变量相对应。例如输入变量为 \[1,2,3] ，则输出变量同样为 \[result-1, result-2, result-3]。

如果选择了**忽略错误并继续，**&#x5F02;常情况的输出值为 null 值，例如 \[result-1, null, result-3]；

如果选择了**移除错误输出，**&#x5C06;不会输出异常变量，例如 \[result-1, result-3]。

### 扩展阅读

[**什么是数组变量？**](../../../learn-more/extended-reading/what-is-array-variable.md)

***

#### 如何生成数组变量？

你可以通过以下节点生成数组变量，用以充当迭代节点的输入变量：

*   [代码节点](code.md)



    <figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/f116ea6a82194dccd88a961324278604.webp" alt="" width="375"><figcaption><p>code 节点输出 array</p></figcaption></figure>
*   [参数提取](parameter-extractor.md)



    <figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/698da93b306ba26998e14b14ad8d2c45.webp" alt="" width="375"><figcaption><p>参数提取节点输出 array</p></figcaption></figure>
* [知识库检索](knowledge-retrieval.md)
* [迭代](iteration.md)
* [工具](tools.md)
* [HTTP 请求](http-request.md)

***

#### 如何将数组转换为文本

迭代节点的输出变量为数组格式，无法直接输出 String 字符串内容。你可以使用一个简单的步骤将数组转换回文本。

**使用代码节点转换**

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/51643d983fd5455b5c8c3ce6f5d63c4b.webp" alt="" width="334"><figcaption><p>代码节点转换</p></figcaption></figure>

代码示例：

```python
def main(articleSections: list):
    data = articleSections
    return {
        "result": "\n".join(data)
    }
```

**使用模板节点转换**

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/node/bca3448a765f2cb2d8a666b9fe55f8ea.webp" alt="" width="332"><figcaption><p>模板节点转换</p></figcaption></figure>

代码示例：

```django
{{ articleSections | join("\n") }}
```
