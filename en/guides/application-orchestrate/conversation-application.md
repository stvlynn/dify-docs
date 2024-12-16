# Conversation Assistant

Conversation applications use a one-question-one-answer mode to have a continuous conversation with the user.

### Applicable scenarios

Conversation applications can be used in fields such as customer service, online education, healthcare, financial services, etc. These applications can help organizations improve work efficiency, reduce labor costs, and provide a better user experience.

### How to compose

Conversation applications supports: prompts, variables, context, opening remarks, and suggestions for the next question.

Here, we use a interviewer application as an example to introduce the way to compose a conversation applications.

#### Step 1 Create an application

Click the "Create Application" button on the homepage to create an application. Fill in the application name, and select **"Chat App"** as the application type.

<figure><img src="https://assets-docs.dify.ai/img/en/application-orchestrate/ec579af36914d43f3b02fae246d83ced.webp" alt=""><figcaption><p>Create Application</p></figcaption></figure>

#### Step 2: Compose the Application

After the application is successfully created, it will automatically redirect to the application overview page. Click on the button on the left menu: **"Orchestrate"** to compose the application.

<figure><img src="https://assets-docs.dify.ai/img/en/application-orchestrate/462987770273f6747dffcd630306c983.webp" alt=""><figcaption></figcaption></figure>

**2.1 Fill in Prompts**

Prompt phrases are used to guide AI in providing professional responses, making the replies more precise. You can utilize the built-in prompt generator to craft suitable prompts. Prompts support the insertion of form variables, such as `{{input}}`. The values in the prompt variables will be replaced with the values filled in by the user.

Example:

1. Enter the interview scenario command.
2. The prompt will automatically generate on the right side content box.
3. You can insert custom variables within the prompt to tailor it to specific needs or details.

For a better experience, we will add an opening dialogue: `"Hello, {{name}}. I'm your interviewer, Bob. Are you ready?"`

To add the opening dialogue, click the "Add Feature" button in the upper left corner, and enable the "Conversation remarkers" feature:

<figure><img src="https://assets-docs.dify.ai/img/en/application-orchestrate/d5c6f07c517c0eeca9611d2add158fe6.webp" alt=""><figcaption></figcaption></figure>

And then edit the opening remarks:

![](https://assets-docs.dify.ai/img/en/application-orchestrate/92f7d07aaa4c86c9e8b59286af602635.webp)

**2.2 Adding Context**

If an application wants to generate content based on private contextual conversations, it can use our [knowledge](../knowledge-base/) feature. Click the "Add" button in the context to add a knowledge base.

![](https://assets-docs.dify.ai/img/en/application-orchestrate/729377b24c0e96977be70d52215c6053.webp)

**2.3 Uploading Documentation File**

Some LLMs now natively support file processing, such as [Claude 3.5 Sonnet](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support) and [Gemini 1.5 Pro](https://ai.google.dev/api/files). You can check the LLMs' websites for details on their file upload capabilities.

Select an LLM that supports file reading and enable the "Documentation" feature. This enables the Chatbot to recognize files without complex configurations.

![](https://assets-docs.dify.ai/2024/11/823399d85e8ced5068dc9da4f693170e.png)


**2.4 Debugging**

Enter user inputs on the right side and check the respond content.

![](https://assets-docs.dify.ai/img/en/application-orchestrate/0a7d50796925831c52decc4eccc069a0.webp)

If the results are not satisfactory, you can adjust the prompts and model parameters. Click on the model name in the upper right corner to set the parameters of the model:

![](https://assets-docs.dify.ai/img/en/application-orchestrate/97051afb0f6a32ad77d8489eb734ffde.webp)

**Debugging with multiple models:**

If debugging with a single model feels inefficient, you can utilize the **Debug as Multiple Models** feature to batch-test the models’ response effectiveness.

![](https://assets-docs.dify.ai/img/en/application-orchestrate/aaba66d00033137b3e0affacab502a93.webp)

Supports adding up to 4 LLMs at the same time.

![](https://assets-docs.dify.ai/img/en/application-orchestrate/66eeff0b9f27dab3d0e5ad28273982ab.webp)

> ⚠️ When using the multi-model debugging feature, if only some large models are visible, it is because other large models’ keys have not been added yet. You can manually add multiple models’ keys in [“Add New Provider”](https://docs.dify.ai/guides/model-configuration/new-provider).

**2.4 Publish App**

After debugging your application, click the **"Publish"** button in the top right corner to create a standalone AI application. In addition to experiencing the application via a public URL, you can also perform secondary development based on APIs, embed it into websites, and more. For details, please refer to [Publishing](https://docs.dify.ai/guides/application-publishing).

If you want to customize the application that you share, you can Fork our open source [WebApp template](https://github.com/langgenius/webapp-conversation). Based on the template, you can modify the application to meet your specific needs and style requirements.
