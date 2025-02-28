# 管理知识库

> 知识库管理页仅面向团队所有者、团队管理员、拥有编辑权限的角色开放。

点击 Dify 平台顶部的 “知识库” 按钮，选择需要管理的知识库。轻点左侧导航中的**设置**进行调整。

你可以在此处调整知识库名称、描述、可见权限、索引模式、Embedding 模型和检索设置。

<figure><img src="https://assets-docs.dify.ai/2024/12/20fc93428f8f20f7acfce665c4ed4ddf.png" alt=""><figcaption><p>知识库设置</p></figcaption></figure>

* **知识库名称**，用于区分不同的知识库。
* **知识库描述**，用于描述知识库内文档代表的信息。
* **可见权限**，提供 **“只有我”** 、**“所有团队成员”** 和 **“部分团队成员”** 三种权限范围。不具有权限的人将无法访问该知识库。若选择将知识库公开至其它成员，则意味着其它成员同样具备该知识库的查看、编辑和删除权限。
* **索引方法**，详细说明请参考[索引方法文档](../create-knowledge-and-upload-documents/setting-indexing-methods.md)。
* **Embedding 模型**， 修改知识库的嵌入模型，修改 Embedding 模型将对知识库内的所有文档重新嵌入，原先的嵌入将会被删除。
* **检索设置**，详细说明请参考[检索设置文档](../create-knowledge-and-upload-documents/setting-indexing-methods.md)。

***

#### 查看知识库内已关联的应用

知识库将会在左侧信息栏中显示已关联的应用数量。将鼠标悬停至圆形信息图标时将显示所有已关联的 Apps 列表，点击右侧的跳转按钮即可快速查看对应的应用。

<figure><img src="https://assets-docs.dify.ai/2024/12/28899b9b0eba8996f364fb74e5b94c7f.png" alt=""><figcaption><p>查看已关联应用</p></figcaption></figure>

***

你可以通过网页维护或 API 两种方式维护知识库内的文档。

#### 维护知识库内文档

支持管理知识库内的文档和对应的文档分段。详细说明请参考以下文档：

{% content-ref url="maintain-knowledge-documents.md" %}
[maintain-knowledge-documents.md](maintain-knowledge-documents.md)
{% endcontent-ref %}

#### 使用 API 维护知识库

Dify 知识库提供整套标准 API ，开发者通过 API 调用对知识库内的文档、分段进行增删改查等日常管理维护操作，请参考以下文档：

{% content-ref url="maintain-dataset-via-api.md" %}
[maintain-dataset-via-api.md](maintain-dataset-via-api.md)
{% endcontent-ref %}

<figure><img src="https://assets-docs.dify.ai//img/zh_CN/knowledge-and-documents-maintenance/aad52cba86e211d5a54337f43faf2ea6.webp" alt=""><figcaption><p>通过 API 管理文档</p></figcaption></figure>
