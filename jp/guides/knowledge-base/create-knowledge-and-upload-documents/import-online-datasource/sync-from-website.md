# Webサイトからデータをインポート

Dify のナレッジベースでは、[Jina Reader](https://jina.ai/reader)や[Firecrawl](https://www.firecrawl.dev/)を利用してウェブページをスクレイピングし、解析したデータをMarkdownの形式でナレッジベースに取り込むことができます。

{% hint style="info" %}
[Jina Reader](https://jina.ai/reader)や[Firecrawl](https://www.firecrawl.dev/)は、オープンソースのウェブページ解析ツールです。ウェブページをクリーンで大規模言語モデル（LLM）が扱いやすいMarkdown形式のテキストに変換します。また、使いやすいAPIサービスも提供しています。
{% endhint %}

## Firecrawl

### Firecrawlの認証情報の設定

右上隅にあるアバターをクリックし、DataSourceページでFirecrawlの認証情報を設定する必要があります。

<figure><img src="https://assets-docs.dify.ai/2024/12/ced8357e468accd1c3f75f451172c1ce.png" alt=""><figcaption></figcaption></figure>

[Firecrawl 公式サイト](https://www.firecrawl.dev/) にログインして登録を完了し、APIキーを取得してから入力し、保存します。

<figure><img src="https://assets-docs.dify.ai/2024/12/e1a854f9b60a429f11181dfb8bcc7990.png" alt=""><figcaption></figcaption></figure>

### Firecrawl を使用してWebコンテンツをクロールする

ナレッジベース作成のページで**Sync from website**を選択し、スクレイピングの対象どしてのウェブページのURLを入力します。

設定項目には、サブページのスクレイピング、スクレイピングするページの上限、ページのスクレイピング深度、ページの除外、指定ページのみのスクレイピング、コンテンツの抽出などが含まれます。設定が完了したら **Run** をクリックし、解析結果のページをプレビューします。

<figure><img src="https://assets-docs.dify.ai/2024/12/3e63b4ced9770e21d5132c3aa8e5d2de.png" alt=""><figcaption><p>Webコンテンツをクロールする</p></figcaption></figure>

解析されたテキストをナレッジベースのドキュメントにインポートし、結果を確認します。**Add URL** をクリックすると、新しいウェブページをさらにインポートできます。

***

## Jina Reader

### Jina Readerの認証情報の設定

右上隅にあるアバターをクリックし、DataSourceページでJina Readerの認証情報を設定する必要があります。

<figure><img src="https://assets-docs.dify.ai/2024/12/ced8357e468accd1c3f75f451172c1ce.png" alt=""><figcaption></figcaption></figure>

[Jina Readerの公式サイト](https://jina.ai/reader) にログインして登録を完了し、APIキーを取得してから入力し、保存します。

<figure><img src="https://assets-docs.dify.ai//img/jp/import-online-datasource/5e2da7fb31eae4015e54a9fd29983539.webp" alt=""><figcaption></figcaption></figure>

### Jina Reader を使用してWebコンテンツをクロールする

ナレッジベース作成のページで**Sync from website**を選択し、スクレイピングの対象どしてのウェブページのURLを入力します。

<figure><img src="https://assets-docs.dify.ai/2024/12/f9170b2a2ab1be94bc85ff3ed3c3e723.png" alt=""><figcaption><p>Webコンテンツをクロールする</p></figcaption></figure>

設定項目には、サブページをクロールするかどうか、クロールされるページ数の上限、サイトマップのクロールを使用するかどうかなどがあります。設定が完了したら **Run** をクリックし、解析結果のページをプレビューします。

<figure><img src="https://assets-docs.dify.ai/2024/12/a875f21a751551c03109c76308c577ee.png" alt=""><figcaption><p>Webコンテンツをクロールする</p></figcaption></figure>

解析されたテキストをナレッジベースのドキュメントにインポートし、結果を確認します。**Add URL** をクリックすると、新しいウェブページをさらにインポートできます。

<figure><img src="https://assets-docs.dify.ai/2024/12/03494dc3c882ac1c74b464ea931e2533.png" alt=""><figcaption><p>Webコンテンツをクロールする</p></figcaption></figure>

クロールが完了すると、Web ページのコンテンツがナレッジ ベースに組み込まれます。