# 应用管理

### 编辑应用信息

创建应用后，如果你想要修改应用名称或描述，可以点击应用左上角的 「编辑信息」 ，重新修改应用的图标、名称或描述。

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/management/0b0391337f7aa4477c02fe09603dad46.webp" alt="zh-Hans-edit-app-info"><figcaption><p>编辑应用信息</p></figcaption></figure>

### 复制应用

应用均支持复制操作，点击应用左上角的 「复制」。


### 导出应用

在 Dify 内创建的应用均支持以 DSL 格式进行导出，你可以自由地将配置文件导入至任意 Dify 团队。

通过以下两种方式导出 DSL 文件。

* 在 “工作室” 页点击应用菜单按钮中 “导出 DSL”；
* 进入应用的编排页后，点击左上角 “导出 DSL”。

![](https://assets-docs.dify.ai//img/zh_CN/management/457a66965cf27bf5960954bba25c96dc.webp)

DSL 文件不包含自定义工具节点内已填写的授权信息，例如第三方服务的 API Key；如果环境变量中包含 `Secret`类型变量，导出文件时将提示是否允许导出该敏感信息。

![](https://assets-docs.dify.ai//img/zh_CN/management/c3b27947ca294bf846af82df0f87ae31.webp)

{% hint style="info" %}
Dify DSL 格式文件是 Dify.AI 定义的 AI 应用工程文件标准，文件格式为 YML。该标准涵盖应用的基本描述、模型参数、编排配置等信息。
{% endhint %}

### 导入应用

将 DSL 文件上传至 Dify 平台内即可完成 Dify 应用的导入。导入 DSL 文件时会进行版本检查，如果导入较低版本的 DSL 文件将进行提示。

- 对于 SaaS 用户而言，在 SaaS 平台导出的 DSL 文件版本为最新版本。
- 对于社区版用户而言，建议参考[更新 Dify](https://docs.dify.ai/zh-hans/getting-started/install-self-hosted/docker-compose#geng-xin-dify)更新社区版以导出更高版本的 DSL 文件，避免潜在的兼容性问题。

![](https://assets-docs.dify.ai/2024/11/487d2c1cc8b86666feb35ea8a346c053.png)

### 删除应用

如果你想要清理应用，可以点击应用左上角的 「删除」 。

{% hint style="info" %}
⚠️ 应用的删除操作无法撤销，所有用户将无法访问你的应用，应用内的所有 Prompt、编排配置和日志均会被删除。
{% endhint %}
