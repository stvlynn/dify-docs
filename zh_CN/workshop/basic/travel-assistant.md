# AI Agent 实战：搭建个人在线旅游助手

> 作者: Steven Lynn。 Dify Technical Writer。

在上一个实验 [如何搭建 AI 图片生成应用](build-ai-image-generation-app.md) 中，我们已初步了解了 Agent 的概念，并且尝试动手写了系统提示词。

本次实验中，我们将继续探索 Agent 的提示词，学习更加规范的提示词撰写方法。

### 本实验中你将掌握的知识点

* 使用 Dify 构建 Agent 的方法
* 结构化的提示词撰写技巧
* 变量的使用方法

### 1. 准备

在新建 Agent 之前，请先确保以下步骤已经完成：

* 注册和登录 [Dify](https://dify.ai)，如果你想要进行本地部署，可以参考 [社区版 - Docker Compose 部署](../../getting-started/install-self-hosted/docker-compose.md)
* 至少配置一个模型供应商（Dify 赠送 200 条 OpenAI 消息额度，但为了确保实验顺利建议自行配置 LLM 的 API Key）

### 2. 配置工具

#### Google

搭建在线旅游助手需要使用联网的搜索引擎作为参考资料来源，本文中将以 Google 作为示例。

当然，你也可以使用其他的搜索引擎，例如[必应](https://docs.dify.ai/zh-hans/guides/tools/tool-configuration/bing)，甚至是由 AI 驱动的 [Perplexity](https://docs.dify.ai/zh-hans/guides/tools/tool-configuration/perplexity)。

Dify 提供的 Google 工具基于 SerpAPI，因此需要提前进入 SerpAPI 的 API Key 管理页申请 API Key 并粘贴到 `Dify - 工具` 的对应位置。

具体操作步骤如下：

1. 新增 SearpAPI 的 API Key：

进入[SearpAPI - API Key](https://serpapi.com/manage-api-key)，如果你尚未注册，会被跳转至进入注册页。

SerpAPI提供一个月100次的免费调用次数，这足够我们完成本次实验了。如果你需要更多的额度，可以增加余额，或者使用其他的开源方案。

点击复制

<figure><img src="../../.gitbook/assets/image (368).png" alt=""><figcaption></figcaption></figure>

2. 前往 **Dify - 工具 - Google**：

点击 `去授权` ，填入API Key并保存。

<figure><img src="../../.gitbook/assets/travel-assistant-1.png" alt=""><figcaption></figcaption></figure>

#### webscraper

本次实验中，我们需要一个爬虫工具从指定的网页中抓取内容，Dify 已提供内置工具，无需额外配置。

<figure><img src="../../.gitbook/assets/travel-assistant-3.png" alt=""><figcaption></figcaption></figure>

#### Wikipedia

我们还希望 Agent 能够准确介绍目的地知识，Wikipedia 是一个比较好知识来源，Dify 也内置了该工具，无需额外配置。

<figure><img src="../../.gitbook/assets/travel-assistant-4.png" alt=""><figcaption></figcaption></figure>

### 3. 构建 Agent

首先我们选择 `创建空白应用 - Agent`：

添加工具：`Google`、`webscraper`和`wikipedia`并启用。

<figure><img src="../../.gitbook/assets/travel-assistant-5.png" alt=""><figcaption></figcaption></figure>

#### 提示词撰写

在撰写提示词时，为了增强 Agent 执行任务的准确性，我们需要撰写结构化的提示词。

一个结构化的提示词通常需要包含以下元素：

- 角色

- 任务

- 示例输出

- 限制

当然，以上的元素不是必须的，你可以根据实际需求来调整提示词。

在撰写时，你可以采用 XML 来构建结构化的提示词，参考 Claude 的这篇文章：[Use XML tags to structure your prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags#example-legal-contract-analysis)。

当然，你也可以使用 Markdown 来构建提示词。对于提示词的撰写并没有一个严格的规范要求。

在下面的内容中，我们将以旅游助手为例，来演示结构化的提示词撰写方法。

1. **角色**

**角色**是为了定义 Agent 的身份和专业领域，确保其回应符合的场景需求。

```
<role>
你是一个专业旅行规划AI助手，具备以下能力：
1. 使用`Google搜索`实时旅行资讯
2. 通过`Wikipedia`验证目的地文化背景
3. 分析用户预算生成个性化方案
4. 用中文输出美观的Markdown格式报告
</role>
```

2. **任务**

**任务**是为了明确 Agent 需要完成的具体工作步骤和流程，指导系统处理用户请求的标准操作程序。

```
<task>
请按以下流程处理用户请求：
1. 信息收集：
   - 确认目的地、出行日期、预算范围
   - 了解用户偏好（文化/自然/美食等）
   - 询问特殊需求（无障碍设施/饮食限制等）

2. 计划制定：
   - 提供3个酒店选项（不同价位）
   - 设计每日行程安排（包含交通路线）
   - 推荐当地特色体验
   - 提示必备物品清单

3. 持续优化：
   - 根据用户反馈调整方案
   - 提供备选计划（应对天气变化等突发情况）
</task>
```

3. **限制**

**限制**是为了设定 Agent 的行为的边界条件，保障输出内容的安全性、准确性和合规性。

```
<constraints>
请严格遵守以下限制：
1. 预算控制：不得推荐超出用户预算30%的选项
2. 安全性：避开近期有旅行警示的地区
3. 客观性：不包含任何商业推广内容
4. 时效性：确保提供的信息有效
</constraints>
```

4. **示例输出**

示例输出不是必要的部分。示例输出的目的是为了给 Agent 一个书写格式的参考，以确保 Agent 的输出更接近我们的期望。

以下是旅游助手的示例输出：

```
<example_output>

### 详细旅行计划

**酒店推荐**
1. 肯辛顿酒店 (了解更多：www.doylecollection.com/hotels/the-kensington-hotel)
- 评分：4.6⭐
- 价格：每晚约350美元
- 简介：坐落在一座摄政时期的联排别墅中，这家优雅的酒店距离南肯辛顿地铁站5分钟步行路程，距离维多利亚和阿尔伯特博物馆10分钟步行路程。

2. 伦勃朗酒店 (了解更多：www.sarova-rembrandthotel.com)
- 评分：4.3⭐
- 价格：每晚约130美元
- 简介：建于1911年，最初是哈罗德百货公司（距离0.4英里）的公寓，这家现代化酒店坐落在维多利亚和阿尔伯特博物馆对面，距离南肯辛顿地铁站（直达希思罗机场）5分钟步行路程。

**第1天 - 抵达和安顿**
- **上午**：抵达机场。欢迎来到你的冒险之旅！我们的代表将在机场迎接你，确保你顺利入住。
- **下午**：入住酒店，稍作休息，恢复精力。
- **晚上**：在住宿周边进行轻松的步行游览，熟悉当地环境。发现附近的用餐选择，享受愉快的第一顿晚餐。

**第2天 - 文化与自然之旅**
- **上午**：从帝国理工学院开始你的一天，这是世界顶尖的学府之一。享受一次校园导览。
- **下午**：选择参观自然历史博物馆（以其引人入胜的展览而闻名）或维多利亚和阿尔伯特博物馆（庆祝艺术和设计）。之后，在宁静的海德公园放松，也许还可以在蛇形湖上乘船游览。
- **晚上**：探索当地美食。我们推荐你在传统的英国酒吧享用晚餐。

**附加服务：**
- **礼宾服务**：在你停留期间，我们的礼宾服务随时可以协助预订餐厅、购买门票、安排交通，以及满足任何特殊要求，以提升你的体验。
- **24/7支持**：我们提供全天候支持，以解决你在旅行中可能遇到的任何问题或需求。

祝你旅途愉快，满载丰富经历和美好回忆！

</example_output>
```

### 思考题 1: 如何规范化用户输入？

通常我们输入 Agent 内容都是自然语言，而自然语言的一个缺点是很难规范化，有可能包含了一些 Agent不需要的信息或者没有价值的信息，这个时候我们可以引入变量来规范化输入。

Dify 目前支持`文本`、`段落`、`下拉选项`、`数字`、`基于 API 的变量`这几种类型的变量。

在本实验中，我们只需要选用`文本`类型的变量即可。

在**变量**中，选择合适的变量类型，我们可以询问用户目的地、旅行天数、预算。

| 变量Key       | 变量类型 | 字段名称 | 可选 |
| ----------- | ---- | ---- | -- |
| destination | 文本   | 目的地  | 是  |
| day         | 文本   | 旅行天数 | 是  |
| budget      | 文本   | 旅行预算 | 是  |

需要注意的是，`变量 Key`，也就是变量的名称，仅支持大小写英文、数字、下划线。`字段名称`是用户可以看到的提示内容。

添加变量后，用户可以按照应用开发者的意图向应用提供必要的背景信息，实现的效果如下：

<figure><img src="../../.gitbook/assets/image (369).png" alt=""><figcaption></figcaption></figure>
