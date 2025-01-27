## モデルプロバイダーの作成

Modelタイプのプラグインを作成する最初のステップは、プラグインプロジェクトを初期化し、モデルプロバイダーファイルを作成することです。その後、具体的な定義済みモデルやカスタムモデルを接続します。

### 事前準備 <a href="#qian-zhi-zhun-bei" id="qian-zhi-zhun-bei"></a>

* Difyプラグインのスキャフォールディングツール
* Python環境（バージョン3.12以上）

プラグイン開発用のスキャフォールディングツールの準備方法については、[開発ツールの初期化](../initialize-development-tools.md)を参照してください。

### 新規プロジェクトの作成 <a href="#chuang-jian-xin-xiang-mu" id="chuang-jian-xin-xiang-mu"></a>

スキャフォールディングツールのコマンドラインから、新しいDifyプラグインプロジェクトを作成します。

```
./dify-plugin-darwin-arm64 plugin init
```

このバイナリファイルを`dify`にリネームし、`/usr/local/bin`にコピーした場合は、次のコマンドで新しいプラグインプロジェクトを作成できます。

```bash
dify plugin init
```

### モデルプラグインテンプレートの選択 <a href="#xuan-ze-cha-jian-lei-xing-he-mu-ban" id="xuan-ze-cha-jian-lei-xing-he-mu-ban"></a>

スキャフォールディングツール内のすべてのテンプレートには、必要なコードが全て含まれています。`LLM`タイプのプラグインテンプレートを選択してください。

![プラグインタイプ: llm](https://assets-docs.dify.ai/2024/12/8efe646e9174164b9edbf658b5934b86.png)

#### プラグイン権限の設定

このLLMプラグインには、次の権限を設定します。

* Models
* LLM
* Storage

![モデルプラグイン権限](https://assets-docs.dify.ai/2024/12/10f3b3ee6c03a1215309f13d712455d4.png)

#### モデルタイプ設定の説明

モデルプロバイダーは、以下の2つのモデル設定方法をサポートしています。

*   `predefined-model` **定義済みモデル**

    一般的な大規模モデルタイプで、統一されたプロバイダー認証情報を設定するだけで、モデルプロバイダーが提供する定義済みモデルを利用できます。たとえば、`OpenAI`モデルプロバイダーは、`gpt-3.5-turbo-0125`や`gpt-4o-2024-05-13`など、様々な定義済みモデルを提供しています。詳細な開発手順については、定義済みモデルの接続を参照してください。
*   `customizable-model` **カスタムモデル**

    各モデルの認証情報設定を手動で追加する必要があります。たとえば、`Xinference`はLLMとText Embeddingの両方をサポートしていますが、各モデルには一意の**model\_uid**があります。両方を同時に接続する場合は、各モデルに**model\_uid**を設定する必要があります。詳細な開発手順については、カスタムモデルの接続を参照してください。

これら2つの設定方法は**共存可能**です。つまり、プロバイダーが`predefined-model`と`customizable-model`の両方、または`predefined-model`のみをサポートしている場合、プロバイダーの統一認証情報を設定することで、定義済みモデルとリモートから取得したモデルを使用できます。さらに、新しいモデルを追加した場合は、それに基づいてカスタムモデルを使用することも可能です。

### 新しいモデルプロバイダーの追加

新しいモデルプロバイダーを追加するには、主に次の手順が必要です。

1.  **モデルプロバイダー設定YAMLファイルの作成**

    プロバイダーディレクトリにYAMLファイルを追加し、プロバイダーの基本情報とパラメータ設定を記述します。ProviderSchemaの要件に従って記述し、システムの仕様との整合性を確保してください。
2.  **モデルプロバイダーコードの記述**

    プロバイダークラスのコードを作成します。システムのインターフェース要件に準拠したPythonクラスを実装して、プロバイダーのAPIに接続し、コア機能を実装します。

***

以下は、各ステップの詳細な操作手順です。

#### 1. **モデルプロバイダー設定ファイルの作成**

ManifestはYAML形式のファイルで、モデルプロバイダーの基本情報、サポートされているモデルタイプ、設定方法、認証情報ルールを定義します。プラグインプロジェクトのテンプレートには、`/providers`パスに設定ファイルが自動的に生成されます。

以下は、`Anthropic`モデルの設定ファイル`anthropic.yaml`のサンプルコードです。

```yaml
provider: anthropic
label:
  en_US: Anthropic
description:
  en_US: Anthropic's powerful models, such as Claude 3.
  zh_Hans: Anthropicの強力なモデル（例：Claude 3）。
icon_small:
  en_US: icon_s_en.svg
icon_large:
  en_US: icon_l_en.svg
background: "#F0F0EB"
help:
  title:
    en_US: Get your API Key from Anthropic
    zh_Hans: AnthropicからAPIキーを取得
  url:
    en_US: https://console.anthropic.com/account/keys
supported_model_types:
  - llm
configurate_methods:
  - predefined-model
provider_credential_schema:
  credential_form_schemas:
    - variable: anthropic_api_key
      label:
        en_US: API Key
      type: secret-input
      required: true
      placeholder:
        zh_Hans: APIキーを入力してください
        en_US: Enter your API Key
    - variable: anthropic_api_url
      label:
        en_US: API URL
      type: text-input
      required: false
      placeholder:
        zh_Hans: API URLを入力してください
        en_US: Enter your API URL
models:
  llm:
    predefined:
      - "models/llm/*.yaml"
    position: "models/llm/_position.yaml"
extra:
  python:
    provider_source: provider/anthropic.py
    model_sources:
      - "models/llm/llm.py"
```

接続するプロバイダーがカスタムモデル（たとえば、`OpenAI`がファインチューニングモデルを提供する場合）を提供する場合は、`model_credential_schema`フィールドを追加する必要があります。

以下は、`OpenAI`ファミリーモデルのサンプルコードです。

```yaml
model_credential_schema:
  model: # ファインチューニングモデル名
    label:
      en_US: Model Name
      zh_Hans: モデル名
    placeholder:
      en_US: Enter your model name
      zh_Hans: モデル名を入力
  credential_form_schemas:
  - variable: openai_api_key
    label:
      en_US: API Key
    type: secret-input
    required: true
    placeholder:
      zh_Hans: APIキーを入力してください
      en_US: Enter your API Key
  - variable: openai_organization
    label:
        zh_Hans: 組織ID
        en_US: Organization
    type: text-input
    required: false
    placeholder:
      zh_Hans: 組織IDを入力してください
      en_US: Enter your Organization ID
  - variable: openai_api_base
    label:
      zh_Hans: API Base
      en_US: API Base
    type: text-input
    required: false
    placeholder:
      zh_Hans: API Baseを入力してください
      en_US: Enter your API Base
```

より詳細なモデルプロバイダーYAMLの仕様については、[モデルインターフェースドキュメント](../../../schema-definition/model/model-schema.md)を参照してください。

#### 2. **モデルプロバイダーコードの記述**

`/providers`フォルダに、同じ名前のPythonファイル（たとえば、`anthropic.py`）を作成し、`__base.provider.Provider`基本クラス（たとえば、`AnthropicProvider`）を継承する`class`を実装します。

以下は、`Anthropic`のサンプルコードです。

```python
import logging
from dify_plugin.entities.model import ModelType
from dify_plugin.errors.model import CredentialsValidateFailedError
from dify_plugin import ModelProvider

logger = logging.getLogger(__name__)


class AnthropicProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        """
        Validate provider credentials

        if validate failed, raise exception

        :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
        """
        try:
            model_instance = self.get_model_instance(ModelType.LLM)
            model_instance.validate_credentials(model="claude-3-opus-20240229", credentials=credentials)
        except CredentialsValidateFailedError as ex:
            raise ex
        except Exception as ex:
            logger.exception(f"{self.get_provider_schema().provider} credentials validate failed")
            raise ex
```

プロバイダーは、`__base.model_provider.ModelProvider`基底クラスを継承し、`validate_provider_credentials`プロバイダー統一認証情報検証メソッドを実装する必要があります。

```python
def validate_provider_credentials(self, credentials: dict) -> None:
    """
    Validate provider credentials
    You can choose any validate_credentials method of model type or implement validate method by yourself,
    such as: get model list api

    if validate failed, raise exception

    :param credentials: provider credentials, credentials form defined in `provider_credential_schema`.
    """
```

もちろん、`validate_provider_credentials`の実装を後回しにして、モデル認証情報検証メソッドの実装後に直接再利用することもできます。

#### **カスタムモデルプロバイダー**

他のタイプのモデルプロバイダーについては、以下の設定方法を参照してください。

`Xinference`のようなカスタムモデルプロバイダーの場合、完全な実装手順を省略できます。`XinferenceProvider`という名前の空のクラスを作成し、その中に空の`validate_provider_credentials`メソッドを実装するだけで済みます。

**詳細説明：**

* `XinferenceProvider`は、カスタムモデルプロバイダーを識別するためのプレースホルダーとして機能します。
* `validate_provider_credentials`メソッドは実際には呼び出されませんが、親クラスが抽象クラスであるため、すべてのサブクラスがこのメソッドを実装する必要があります。空の実装を提供することで、抽象メソッドが実装されていないことによるインスタンス化エラーを回避できます。

```python
class XinferenceProvider(Provider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        pass
```

モデルプロバイダーを初期化した後、プロバイダーが提供する具体的なLLMモデルを接続する必要があります。詳細については、以下を参照してください。

* [定義済みモデルの接続](../../../../guides/model-configuration/predefined-model.md)
* [カスタムモデルの接続](../../../../guides/model-configuration/customizable-model.md)