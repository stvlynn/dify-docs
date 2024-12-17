# Tools

The workflow provides a rich selection of tools, categorized into three types:

* **Built-in Tools**: Tools provided by Dify.
* **Custom Tools**: Tools imported or configured via the OpenAPI/Swagger standard format.
* **Workflows**: Workflows that have been published as tools.

## Add and Use the Tool Node

Before using built-in tools, you may need to **authorize** the tools.

If built-in tools do not meet your needs, you can create custom tools in the **Dify menu navigation -- Tools** section.

You can also orchestrate a more complex workflow and publish it as a tool.

<figure><img src="https://assets-docs.dify.ai/img/en/node/1abdf412e44dab82cad75f3009676ab6.webp" alt="" width="258"><figcaption><p>Tool Selection</p></figcaption></figure>

<figure><img src="https://assets-docs.dify.ai/img/en/node/680957fc907e2e0be1390c3043bd6d24.webp" alt=""><figcaption><p>Configuring Google Search Tool to Retrieve External Knowledge</p></figcaption></figure>

Configuring a tool node generally involves two steps:

1. Authorizing the tool/creating a custom tool/publishing a workflow as a tool.
2. Configuring the tool's input and parameters.

For more information on how to create custom tools and configure them, please refer to the [Tool Configuration Guide](https://docs.dify.ai/guides/tools).

### Advanced Features

Tool nodes may encounter errors during information processing that could interrupt the workflow. Developers can follow these steps to configure fail branches, enabling contingency plans when nodes encounter exceptions, avoiding workflow interruptions.

1. Enable "Error Handling" in the tool node
2. Select and configure an error-handling strategy

![](https://assets-docs.dify.ai/2024/12/39dc3b5881d9a5fe35b877971f70d3a6.png)

For more information about exception handling approaches, please refer to [Error Handling](https://docs.dify.ai/guides/workflow/error-handling).

## Publishing Workflow Applications as Tools

Workflow applications can be published as tools and used by nodes in other workflows. For information about creating custom tools and tool configuration, please refer to the [Tool Configuration Guide](https://docs.dify.ai/guides/tools).
