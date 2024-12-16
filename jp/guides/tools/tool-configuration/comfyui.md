# ComfyUI

[ComfyUI](https://www.comfy.org/)は、最強のモジュラー型拡散モデルのGUI、API、バックエンドを備えたツールで、グラフやノードインターフェースを提供します。現在、Difyで利用可能で、画像のプロンプトを入力することで生成された画像を取得できます。

## 1. ComfyUIのワークフローが正しく動作しているか確認します。
ComfyUIが正常に動作し、画像が生成されることを確かめるためには、[公式ドキュメント](https://docs.comfy.org/get_started/gettingstarted)を参照してください。

## 2. Prompt 設定

Difyを介してプロンプトを渡す必要がない場合は、この手順をスキップできます。プロンプトノードが ComfyUI の唯一の `KSampler` ノードに接続されている場合は、この手順もスキップできます。
それ以外の場合は、ポジティブなプロンプトの単語の内容を置き換えるには文字列 `{{positive_prompt}}` を使用し、ネガティヴなプロンプトの単語の内容を置き換えるには `{{negative_prompt}}` を使用してください。
<figure><img src="https://assets-docs.dify.ai/img/jp/tool-configuration/2ae273f9a6edbc583b3176340f8ae416.webp" alt=""><figcaption></figcaption></figure>

## 3. ワークフローのAPIファイルをエクスポートします。
<figure><img src="https://assets-docs.dify.ai/img/jp/tool-configuration/d9208896a45c4fedd6b4390cf647f512.webp" alt=""><figcaption></figcaption></figure>
画像のように、「Save (API Format)」を選択してください。このオプションが表示されない場合は、設定で「Dev Mode」を有効にする必要があります。

## 4. DifyにComfyUIを統合します。
Difyのナビゲーションページで、`ツール > ComfyUI > 認証する`の順にクリックし、API キーを入力してください。DifyのDocker展開を使用している場合、このアドレスは通常 `http://host.docker.internal:8188` です。

## 5. DifyでComfyUIを利用します。
`Workflow`ツールを開き、エクスポートしたAPIファイルの内容を `WORKFLOW JSON` に入力して、通常通りに生成を行ってください。