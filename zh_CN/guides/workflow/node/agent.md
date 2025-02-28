# Agent

## 定义

Agent 节点是 Dify Chatflow/Workflow 中用于实现自主工具调用的组件。它通过集成不同的 Agent 推理策略，使大语言模型能够在运行时动态选择并执行工具，从而实现多步推理。

## 配置步骤

### 添加节点

在 Dify Chatflow/Workflow 编辑器中，从组件栏拖拽 Agent 节点至画布。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/efa82daba2da8e59ee1b867744977f3d.webp" alt=""><figcaption></figcaption></figure>

### 选择 Agent 策略

在节点配置面板中，点击 **Agent 策略**。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/4b377b9ec51d63e492b50f13f17a700c.webp" alt=""><figcaption></figcaption></figure>

从下拉菜单选择所需的 Agent 推理策略。Dify 内置了 **Function Calling 和 ReAct** 两种策略，可在 **Marketplace** → **Agent 策略**分类中安装使用。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/38fec180c23b6ba3d33e695e223ec9dc.webp" alt=""><figcaption></figcaption></figure>

#### 1. Function Calling

通过将用户指令映射到预定义函数或工具，LLM 先识别用户意图，再决定调用哪个函数并提取所需参数。它的核心是调用外部函数或工具，属于一种明确的工具调用机制。

**优点:**

* **精确:** 对于明确的任务，可以直接调用相应的工具，无需复杂的推理过程。
* **易于集成外部功能:** 可以将各种外部 API 或工具封装成函数供模型调用。
* **结构化输出:** 模型输出的是结构化的函数调用信息，方便下游节点处理。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/1304dc7ff50293f11010368300cc2a11.webp" alt=""><figcaption></figcaption></figure>

2. **ReAct (Reason + Act)**

ReAct 策略使 Agent 交替进行思考和行动：LLM 首先思考当前状态和目标，然后选择并调用合适的工具，工具的输出结果又将引导 LLM 进行下一步的思考和行动，如此循环，直到问题解决。

**优点:**

* **有效利用外部信息:** 能够有效地利用外部工具获取信息，解决仅靠模型自身无法完成的任务。
* **可解释性较好:** 思考和行动的过程是交织的，可以一定程度上追踪 Agent 的推理路径。
* **适用范围广:** 适用于需要外部知识或需要执行特定操作的场景，例如问答、信息检索、任务执行等。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/7af72a99e9915b97927d0d6ce9672ed2.webp" alt=""><figcaption></figcaption></figure>

开发者可以向[公开仓库](https://github.com/langgenius/dify-plugins)贡献 Agent 策略插件，经过审核后将在 Marketplace 上架，供其他用户安装使用。

### **配置节点参数**

选择 Agent 策略后，配置面板会显示对应的配置项。Dify 官方内置的 Function Calling 和 ReAct 策略的配置项包括：

1. **模型：** 选择驱动 Agent 的大语言模型。
2. **工具：** 工具的使用方式由 Agent 策略定义，点击 "+" 添加并配置 Agent 可调用的工具。
   * **搜索：** 在下拉框中选择已安装的工具插件。
   * **授权：** 填写 API 密钥等授权信息后启用工具。
   * **工具描述和参数设置：** 提供工具描述，帮助 LLM 理解工具用途并选择调用，同时设置工具的功能参数。
3. **指令：** 定义 Agent 的任务目标和上下文。支持使用 Jinja 语法引用上游节点变量。
4. **查询：** 接收用户输入。
5. **最大迭代次数：** 设定 Agent 的最大执行步数。
6. **输出变量：** 提示节点输出的数据结构。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/be202630a2f5222350dcef165e893f33.webp" alt=""><figcaption></figcaption></figure>

## **查看日志**

Agent 节点执行过程中将生成详细日志。显示节点执行的总体信息，包括输入和输出、token 开销、耗时和状态。点击 "详情" 查看 Agent 策略执行的每一轮输出信息。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/node/7d57706bc879341218e63e5cd8223978.webp" alt=""><figcaption></figcaption></figure>
