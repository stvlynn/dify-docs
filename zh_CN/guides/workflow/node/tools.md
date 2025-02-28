# 工具

“工具”节点可以为工作流提供强大的第三方能力支持，分为以下三种类型：

* **内置工具**，Dify 第一方提供的工具，使用该工具前可能需要先给工具进行 **授权**。
* **自定义工具**，通过 [OpenAPI/Swagger 标准格式](https://swagger.io/specification/)导入或配置的工具。如果内置工具无法满足使用需求，你可以在 **Dify 菜单导航 --工具** 内创建自定义工具。
* **工作流**，你可以编排一个更复杂的工作流，并将其发布为工具。详细说明请参考[工具配置说明](https://docs.dify.ai/v/zh-hans/guides/tools)。

## 添加并使用工具节点

添加节点时，选择右侧的 “工具” tab 页。配置工具节点一般分为两个步骤：

1. 对工具授权/创建自定义工具/将工作流发布为工具
2. 配置工具输入和参数

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/6bfdc7ed8255c7915b0f1f9aae8f784f.webp" alt="" width="258"><figcaption><p>工具选择</p></figcaption></figure>

工具节点可以连接其它节点，通过[变量](https://docs.dify.ai/v/zh-hans/guides/workflow/variables)处理和传递数据。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/95ce7380cf2aaad26074369c4da4975b.webp" alt=""><figcaption><p>配置 Google 搜索工具检索外部知识</p></figcaption></figure>

### 高级功能

**错误重试**

针对节点发生的部分异常情况，通常情况下再次重试运行节点即可解决。开启错误重试功能后，节点将在发生错误的时候按照预设策略进行自动重试。你可以调整最大重试次数和每次重试间隔以设置重试策略。

- 最大重试次数为 10 次
- 最大重试间隔时间为 5000 ms

![](https://assets-docs.dify.ai/2024/12/34867b2d910d74d2671cd40287200480.png)

**异常处理**

工具节点处理信息时有可能会遇到异常情况，导致流程中断。应用开发者可以参考以下步骤配置异常分支，在节点出现异常时启用应对方案，而避免中断整个流程。

1. 在工具节点启用 “异常处理”
2. 选择异常处理方案并进行配置

![](https://assets-docs.dify.ai/2024/12/39dc3b5881d9a5fe35b877971f70d3a6.png)

需了解更多应对异常的处理办法，请参考[异常处理](https://docs.dify.ai/zh-hans/guides/workflow/error-handling)。

## 将工作流应用发布为工具

工作流应用可以被发布为工具，并被其它工作流内的节点所应用。关于如何创建自定义工具和配置工具，请参考[工具配置说明](https://docs.dify.ai/v/zh-hans/guides/tools)。
