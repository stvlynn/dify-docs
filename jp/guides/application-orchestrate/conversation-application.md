# 会話型アプリケーション

会話型アプリケーションは、ユーザーとの継続的な対話を一問一答形式で行います。

### 適用シーン

会話型アプリケーションは、カスタマーサービス、オンライン教育、医療、金融サービスなどの分野で利用されることがあります。これらのアプリケーションは、組織の業務の効率を向上させたり、人件費を削減したり、ユーザーエクスペリエンスを高めるのに寄与します。

### 編成方法

会話型アプリケーションの作成には、プロンプト、変数、コンテキスト、オープニングダイアログ、次の質問の提案などが含まれています。

ここでは、**面接官**用のアプリケーションを例に使って、会話型アプリケーションの編成方法を紹介します。

#### アプリケーションの作成

ホームページで「最初から作成」をクリックしてアプリケーションを作成します。アプリケーション名を入力し、アプリタイプは**チャットボット**を選択します。

<figure><img src="https://assets-docs.dify.ai/img/jp/application-orchestrate/08697025dd7176cdc50ff0c0bf3ad90b.webp" alt=""><figcaption><p>チャットボットの作成</p></figcaption></figure>

#### アプリケーションの編成

アプリケーションを作成すると、自動的にアプリケーションの概要ページに移動します。左側のメニューから編成をクリックしてアプリケーションを編成します。

<figure><img src="https://assets-docs.dify.ai/img/jp/application-orchestrate/72b58f4207dfeea6abb5b65aea3be45e.webp" alt=""><figcaption><p>アプリケーションの編成</p></figcaption></figure>

**プロンプトの記入**

プロンプトは、AIが専門的な回答を行う範囲を制限し、回答をより正確にします。組み込みのプロンプトジェネレータを使用して、適切なプロンプトを作成することができます。プロンプト内には、たとえば `{{input}}` のようなフォーム変数を挿入することができます。変数内の値は、ユーザーが入力した値に置き換えられます。

例：

1. インタビューシナリオの指示を入力します。
2. プロンプトが自動的に右側の内容欄に生成されます。
3. カスタム変数をプロンプトに挿入することで、特定の要望や詳細に応じてカスタマイズが可能です。

ユーザーエクスペリエンスを向上させるために、オープニングダイアログを追加することができます：`こんにちは、{{name}}さん。私はあなたの面接官、Bobです。準備はできていますか？`。ページ下部の「機能の追加」ボタンをクリックして、「オープニングダイアログ」機能を開きます

オープニングダイアログを追加する方法は、底の「機能を追加」ボタンをクリックして、「会話の開始」機能を開きます：

<figure><img src="https://assets-docs.dify.ai/img/jp/application-orchestrate/e6956c649c9db22edebd7b03d6fedac8.webp" alt=""><figcaption></figcaption></figure>

オープニングステートメントを編集する際に、いくつかのオープニング質問を追加することもできます：

![](https://assets-docs.dify.ai/img/jp/application-orchestrate/47692893b656f29e1f2b7b72ac644870.webp)

#### コンテキストの追加

AIの対話範囲を[ナレッジベース](../knowledge-base/)内に制限したい場合、企業内のカスタマーサービス用語規準などを「コンテキスト」で参照することができます。

![](https://assets-docs.dify.ai/img/jp/application-orchestrate/3f135004de6416229d71ea8d68955554.webp)

### ファイルのアップロード

Claude 3.5 Sonnet (https://docs.anthropic.com/en/docs/build-with-claude/pdf-support) や Gemini 1.5 Pro (https://ai.google.dev/api/files) など、一部のLLMはファイル処理に標準対応しています。各LLMのウェブサイトで、ファイルのアップロード機能について詳しくご確認ください。

ファイルの読み込みに対応したLLMを選択し、「Document」を有効にしてください。これにより、チャットボットは複雑な設定なしでファイルの内容を理解し、利用できるようになります。

![](https://assets-docs.dify.ai/2024/11/823399d85e8ced5068dc9da4f693170e.png)

#### デバッグ

右側にユーザー入力項目を入力し、内容を入力してデバッグします。

![](https://assets-docs.dify.ai/img/jp/application-orchestrate/9e1f448224130626ae1b7b5acf0f8622.webp)

回答結果が望ましくない場合は、プロンプトやモデルを調整することができます。また、複数のモデルを同期してデバッグすることもでき、適切な構成を組み合わせることができます。

![](https://assets-docs.dify.ai/img/jp/application-orchestrate/5738f1cdddd5ce3e003c3d683d88ecfb.webp)

**複数のモデルでのデバッグ：**

単一モデルでのデバッグが効率的ではない場合、**「複数のモデルでのデバッグ」**機能を使用して、複数のモデルの回答効果を一括確認することもできます。

![](https://assets-docs.dify.ai/img/jp/application-orchestrate/2f379caf3d5de459cca0f64969bfce80.webp)

最大4つの大きなモデルを同時に追加できます。

![](https://assets-docs.dify.ai/img/jp/application-orchestrate/599b64757a2628258b88200cfffd5e48.webp)

> ⚠️ 複数モデルでデバッグ機能を使用する際に、一部の大きなモデルしか表示されない場合は、他の大きなモデルのキーが追加されていないためです。["新しいプロバイダーの追加"](https://docs.dify.ai/v/ja-jp/guides/model-configuration/new-provider)で、複数のモデルのキーを手動で追加できます。

#### アプリケーションの公開

アプリケーションのデバッグが完了したら、右上の**公開**ボタンをクリックして独立したAIアプリケーションを生成します。公開URLを使用してアプリケーションを体験するだけでなく、APIベースの開発やWebサイトへの組み込みなども行うことができます。詳細については[公開](https://docs.dify.ai/v/ja-jp/guides/application-publishing)を参照してください。

公開されたアプリケーションをカスタマイズしたい場合は、当社のオープンソースの[WebAppテンプレート](https://github.com/langgenius/webapp-conversation)をForkしてください。テンプレートをベースに、シチュエーションやスタイルに合わせたアプリケーションを作成できます。

### よくある質問

**チャットアシスタント内にサードパーティツールを追加するにはどうすればよいですか? **

チャット アシスタント タイプのアプリケーションは、サードパーティ ツールの追加をサポートしていません。[エージェント](https://docs.dify.ai/v/ja-jp/guides/application-orchestrate/agent) 内でサードパーティ ツールを追加できます。アプリケーション。
