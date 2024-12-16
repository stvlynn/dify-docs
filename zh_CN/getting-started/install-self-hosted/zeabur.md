# 部署 Dify 到 Zeabur

[Zeabur](https://zeabur.com) 是一个服务部署平台，可以通过一键部署的方式部署 Dify。本指南将指导你如何将 Dify 部署到 Zeabur。

## 前置要求

在开始之前，你需要以下内容：

- 一个 Zeabur 账户。如果你没有账户，可以在 [Zeabur](https://zeabur.com/) 注册一个免费账户。
- 升级你的 Zeabur 账户到开发者计划（每月 5 美元）。你可以从 [Zeabur 定价](https://zeabur.com/pricing) 了解更多信息。

## 部署 Dify 到 Zeabur

Zeabur 团队准备了一个一键部署模板，你只需点击下面的按钮即可开始：

[![Deploy to Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/1D4DOW)

点击按钮后，你将被导航到 Zeabur 上的模板页面，你可以在那里查看部署的详细信息和说明。

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/install-self-hosted/4f2451c684f691815930b830d57e2446.webp" alt="Zeabur Template Overview"><figcaption></figcaption></figure>

点击部署按钮后，你需要输入一个生成的域名，以便将域名绑定到你的 Dify 实例并注入到其他服务中作为环境变量。
然后选择你喜欢的区域，点击部署按钮，你的 Dify 实例将在几分钟内部署完成。

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/install-self-hosted/b23726cca84bb2617f39809b4d123c54.webp" alt="Select Region"><figcaption></figcaption></figure>

部署完成后，你可以在 Zeabur 控制台中看到一个项目页面，如下图所示，你在部署过程中输入的域名将自动绑定到 NGINX 服务，你可以通过该域名访问你的 Dify 实例。

<figure><img src="https://assets-docs.dify.ai/img/zh_CN/install-self-hosted/b3c19c1bfe1ef9d955b8e57fb64d1119.webp" alt="Zeabur Project Overview"><figcaption></figcaption></figure>

你也可以在 NGINX 服务页面的 Networking 选项卡中更改域名。你可以参考 [Zeabur 文档](https://zeabur.com/docs/deploy/domain-binding) 了解更多信息。