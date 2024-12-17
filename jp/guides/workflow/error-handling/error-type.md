# エラータイプの概要

本記事では、さまざまなノードで発生可能なトラブルと、それに伴うエラーの種類について解説します。

## チャットフロー／ワークフロー

* **システムエラー**
  システム関連の問題が原因で発生するエラーです。例えば、サービスが正しく起動していない、ネットワーク接続に問題がある場合などが該当します。

* **操作エラー**
  開発者がノードの設定や操作に失敗した際に生じるエラーです。

## コードノード
[コードノード](../node/code.md)を使用することで、PythonやJavaScriptのコードを実行し、データ変換を行うことができます。ここでは、よくある4つのエラーを紹介します：

1. **コードエラー（CodeNodeError）**
   開発者のコード内で例外が発生した場合にこのエラーが起きます。変数が不足している、計算ロジックが間違っている、文字列として扱うべき配列を誤って変数として扱っている場合などがあります。エラーメッセージや具体的な行番号で問題を特定できます。

   <figure><img src="https://assets-docs.dify.ai/2024/12/c86b11af7f92368180ea1bac38d77083.png" alt=""><figcaption><p>コードエラー</p></figcaption></figure>

2. **サンドボックスのネットワーク問題（System Error）**
   ネットワークのトラフィック異常や接続問題によって生じるエラーです。サンドボックスサービスが停止している、プロキシがネットワークをブロックしている場合などです。この問題は次の手順で解決可能です：
   a. ネットワークの品質を確認する
   b. サンドボックスサービスを再起動する
   c. プロキシ設定を見直す

   <figure><img src="https://assets-docs.dify.ai/2024/12/d95007adf67c4f232e46ec455c348e2c.PNG" alt=""><figcaption><p>サンドボックスのネットワーク問題</p></figcaption></figure>

3. **ネスト制限エラー（DepthLimitError）**
   現在のノードは、最大で5層までのネスト構造をサポートしています。これを超えるとエラーが発生します。

   <figure><img src="https://assets-docs.dify.ai/2024/12/5649d52a6e80ddd4180b336266701f7b.png" alt=""><figcaption><p>DepthLimitError</p></figcaption></figure>

4. **出力検証エラー（OutputValidationError）**
   選択した出力変数の型と実際の出力変数の型が一致しない場合に生じるエラーです。開発者は適切な出力変数の型を選択し直すことで、この問題を回避することができます。

   <figure><img src="https://assets-docs.dify.ai/2024/12/ab8cae01a590b037017dfe9ea4dbbb8b.png" alt=""><figcaption><p>OutputValidationError</p></figcaption></figure>

## LLMノード

[LLMノード](../node/llm.md)は、チャットフローやワークフローの中核をなすコンポーネントであり、大規模言語モデルを用いて様々なタスクを処理します。

以下は、実行時に遭遇する可能性のある6つの一般的なエラーです：

1. **変数が見つからない（VariableNotFoundError）**
   システムプロンプトやコンテキストで指定された変数がLLMによって見つけられない場合にこのエラーが発生します。開発者は、補足となる変数を設定することで問題を解決できます。

   <figure><img src="https://assets-docs.dify.ai/2024/12/f20c5fbde345144de6183374ab277662.png" alt=""><figcaption><p>VariableNotFoundError</p></figcaption></figure>

2. **コンテキスト構造の無効 (InvalidContextStructureError)**
   LLMノードが不正なデータ構造を受け取った場合に報告されます。コンテキストは文字列データ構造のみをサポートします。

3. **無効な変数タイプ（InvalidVariableTypeError）**
   システムプロンプトの形式が一般的なテキストやJinja syntaxでない場合にこのエラーが生じます。

4. **モデルが存在しない（ModelNotExistError）**
   各LLMノードにはモデルの指定が必要です。モデルが選択されていない場合には、このエラーが発生します。

5. **LLMの認証が必要（LLMModeRequiredError）**
   選択されたモデルにAPIキーが設定されていない場合にこのエラーが報告されます。ドキュメントの指示に従ってモデルを認証してください。

6. **プロンプトが見つからない（NoPromptFoundError）**
   LLMノードのプロンプトが空の場合、エラーが生じます。

## HTTPノード

[HTTPノード](../node/http-request.md)は、HTTPリクエストを送信してデータを取得、Webhookを発火、画像を生成、ファイルをダウンロードするなどの操作を可能にし、カスタマイズ可能なリクエストによって外部サービスとのシームレスな統合を実現します。ここでは、このノードで頻繁に発生する5つの一般的なエラーを紹介します：

1. **認証設定エラー（AuthorizationConfigError）**  
   認証情報が設定されていない場合に発生するエラーです。

2. **ファイル取得エラー（FileFetchError）**  
   ファイル変数が取得できない場合に発生するエラーです。

3. **不正なHTTPリクエストメソッド（InvalidHttpMethodError）**  
   リクエストメソッドがGET、HEAD、POST、PUT、PATCH、DELETEのいずれにも該当しない場合にエラーが発生します。

4. **レスポンスサイズ超過（ResponseSizeError）**  
   HTTPレスポンスが10MBの制限を超えると、このエラーが発生します。

5. **HTTPレスポンスコードエラー（HTTPResponseCodeError）**  
   レスポンスコードが200系以外（例：400、404、500など）の場合にエラーが報告されます。例外処理が有効であれば、これらのステータスコードによるエラーが報告されますが、それ以外ではエラーは報告されません。

## ツールノード

ランタイムでよく遭遇する3つのエラーは以下のとおりです：

1. **ツール実行エラー（ToolNodeError）**  
   ツール自体の実行に問題があった場合に報告されるエラーです。たとえば、目指すAPIのリクエスト制限に達した場合などがこれに該当します。

   <figure><img src="https://assets-docs.dify.ai/2024/12/84af0831b7cb23e64159dfbba80e9b28.jpg" alt=""><figcaption></figcaption></figure>

2. **ツールパラメータエラー（ToolParameterError）**  
   ツールノードの設定パラメータに問題がある場合、つまりツールノードが要求するパラメータと異なる値が入力された場合にこのエラーが発生します。

3. **ツールファイル処理エラー（ToolFileError）**  
   ツールノードの処理に必要なファイルが見つからない場合にこのエラーが発生します。