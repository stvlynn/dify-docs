# シングルページWebアプリとして公開

Difyを使ってAIアプリを作成するメリットの一つは、数分でユーザー向けのWebアプリを公開できることです。このアプリはあなたのプロンプトに基づいて機能します。

* 自己ホストのオープンソース版を使用する場合、そのアプリはあなたのサーバー上で動作します
* クラウドサービスを使用する場合、そのアプリはUdify.appにホストされます

***

### AIサイトの公開

アプリ概要ページで、AIサイト（Webアプリ）に関するカードを見つけることができます。Webアプリのアクセスをオンにするだけで、ユーザーと共有できるリンクが得られます。

<figure><img src="https://assets-docs.dify.ai/img/jp/launch-your-webapp-quickly/f3f0401a568778f8663934e518d85ffd.webp" alt=""><figcaption></figcaption></figure>

以下の2種類のアプリには、きれいなWebアプリのインターフェースを提供しています：

* テキスト生成型（[前往预览](text-generator.md)）
* 対話型（[前往预览](conversation-application.md)）

***

### AIサイトの設定

Webアプリのカード上の**設定**ボタンをクリックすると、AIサイトのオプションをいくつか設定できます。これらは最終ユーザーに表示されます：

* アイコン
* 名前
* アプリの説明
* インターフェース言語
* 著作権情報
* プライバシーポリシーリンク
* カスタム免責事項

{% hint style="info" %}
現在サポートされているインターフェース言語：英語、中国語（簡体字）、中国語（繁体字）、ポルトガル語、ドイツ語、日本語、韓国語、ウクライナ語、ベトナム語。追加の言語が必要な場合は、GitHubでイシューを提出するか、プルリクエストを提出してコードを提供してください。[サポートを求める](../../../community/support.md)。
{% endhint %}

***

### AIサイトの埋め込み

Difyは、あなたのAIアプリをビジネスWebサイトに埋め込むことをサポートしています。この機能を使えば、数分でビジネスデータを持つ公式サイトのAIカスタマーサポートやビジネス知識Q&Aなどのアプリを作成できます。Webアプリのカード上の埋め込みボタンをクリックし、埋め込みコードをコピーして、Webサイトの目標位置に貼り付けます。

*   iframeタグの方法

    iframeコードを、AIアプリを表示するあなたのWebサイトのタグ（例：`<div>`、`<section>`）にコピーします。
*   scriptタグの方法

    scriptコードを、あなたのWebサイトの`<head>`または`<body>`タグにコピーします。

<figure><img src="https://assets-docs.dify.ai/img/jp/launch-your-webapp-quickly/1727828fefce51c99339f1e2d977ce88.webp" alt=""><figcaption></figcaption></figure>

例えば、scriptコードを公式サイトの`<body>`に貼り付けると、公式サイトのAIロボットが得られます：

<figure><img src="https://assets-docs.dify.ai/img/jp/launch-your-webapp-quickly/3323f6d44761d383ef60ff7a1d14e4ac.webp" alt=""><figcaption></figcaption></figure>