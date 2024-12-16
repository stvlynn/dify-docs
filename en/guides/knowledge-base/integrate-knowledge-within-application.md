# Integrate Knowledge Base within Application

### Creating an Application Integrated with Knowledge Base

A **"Knowledge Base"** can be used as an external information source to provide precise answers to user questions via LLM. You can associate an existing knowledge base with any [application type](https://docs.dify.ai/guides/application-orchestrate#application\_type) in Dify.

Taking a chat assistant as an example, the process is as follows:

1. Go to **Knowledge -- Create Knowledge -- Upload file**
2. Go to **Studio -- Create Application -- Select Chatbot**
3. Enter **Context**, click **Add**, and select one of the knowledge base created
4. In **Context Settings -- Retrieval Setting**, configure the **Retrieval Setting**
5. Enable **Citation and Attribution** in **Add Features**
6. In **Debug and Preview**, input user questions related to the knowledge base for debugging
7. After debugging, click **Publish** button to make an AI application based on your own knowledge!

***

### Connecting Knowledge and Setting Retrieval Mode

In applications that utilize multiple knowledge bases, it is essential to configure the retrieval mode to enhance the precision of retrieved content. To set the retrieval mode for the knowledge bases, navigate to **Context -- Retrieval Settings -- Rerank Setting**.

#### Retrieval Setting

The retriever scans all knowledge bases linked to the application for text content relevant to the user's question. The results are then consolidated. Below is the technical flowchart for the Multi-path Retrieval mode:

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/cf9b4d10e65ad7d0e42b9c69045da709.webp" alt=""><figcaption></figcaption></figure>

This method simultaneously queries all knowledge bases connected in **"Context"**, seeking relevant text chucks across multiple knowledge bases, collecting all content that aligns with the user's question, and ultimately applying the Rerank strategy to identify the most appropriate content to respond to the user. This retrieval approach offers more comprehensive and accurate results by leveraging multiple knowledge bases simultaneously.

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/200496cb1677e73dab28007c74b044a9.webp" alt=""><figcaption></figcaption></figure>

For instance, in application A, with three knowledge bases K1, K2, and K3. When a user send a question, multiple relevant pieces of content will be retrieved and combined from these knowledge bases. To ensure the most pertinent content is identified, the Rerank strategy is employed to find the content that best relates to the user's query, enhancing the precision and reliability of the results.

In practical Q\&A scenarios, the sources of content and retrieval methods for each knowledge base may differ. To manage the mixed content returned from retrieval, the [Rerank strategy](https://docs.dify.ai/learn-more/extended-reading/retrieval-augment/rerank) acts as a refined sorting mechanism. It ensures that the candidate content aligns well with the user's question, optimizing the ranking of results across multiple knowledge bases to identify the most suitable content, thereby improving answer quality and overall user experience.

Considering the costs associated with using Rerank and the needs of the business, the multi-path retrieval mode provides two Rerank settings:

**Weighted Score**

This setting uses internal scoring mechanisms and does not require an external Rerank model, thus **avoiding any additional processing costs**. You can select the most appropriate content matching strategy by adjusting the weight ratio sliders for semantics or keywords.

*   **Semantic Value of 1**

    This mode activates semantic retrieval only. By utilizing the Embedding model, the search depth can be enhanced even if the exact words from the query do not appear in the knowledge base, as it calculates vector distances to return the relevant content. Furthermore, when dealing with multilingual content, semantic retrieval can capture meanings across different languages, yielding more accurate cross-language search results.
*   **Keyword Value of 1**

    This mode activates keyword retrieval only. It matches the user's input text against the full text of the knowledge base, making it ideal for scenarios where the user knows the exact information or terminology. This method is resource-efficient, making it suitable for quickly retrieving information from large document repositories.
*   **Custom Keyword and Semantic Weights**

    In addition to enabling only semantic or keyword retrieval modes, we offer flexible custom Weight Score. You can determine the best weight ratio for your business scenario by continuously adjusting the weights of both.

**Rerank Model**

The Rerank model is an external scoring system that calculates the relevance score between the user's question and each candidate document provided, improving the results of semantic ranking and returning a list of documents sorted by relevance from high to low.

While this method incurs some additional costs, it is more adept at handling complex knowledge base content, such as content that combines semantic queries and keyword matches, or cases involving multilingual returned content.

> Click here to learn more about the [Re-ranking](https://docs.dify.ai/learn-more/extended-reading/retrieval-augment/rerank).

Dify currently supports multiple Rerank models. To use external Rerank models, you'll need to provide an API Key. Enter the API Key for the Rerank model (such as Cohere, Jina AI, etc.) on the "Model Provider" page.

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/6b959d7417b18420b68da01fdd0ba2a5.webp" alt=""><figcaption><p>Configuring the Rerank model in the Model Provider</p></figcaption></figure>

**Adjustable Parameters**

*   **TopK**

    This parameter filters the text segments that are most similar to the user's question. The system dynamically adjusts the number of segments based on the context window size of the selected model. A higher value results in more text segments being recalled.
*   **Score Threshold**

    This parameter establishes the similarity threshold for filtering text segments. Only those segments with a vector retrieval similarity score exceeding the set threshold will be recalled. A higher threshold value results in fewer texts being recalled, but those recalled are likely to be more relevant. Adjust this parameter based on your specific needs for precision versus recall.

The multi-recall mode can achieve higher quality recall results when retrieving from multiple knowledge bases; therefore, it is **recommended to set the recall mode to multi-recall**.

### Frequently Asked Questions

Here's the translation of the provided content:

1. **How should I choose Rerank settings in multi-recall mode?**

If users know the exact information or terminology, and keyword retrieval can accurately deliver matching results, set the **Keyword to 1** in the "Weight Score".

If the exact vocabulary does not appear in the knowledge base, or if there are cross-language queries, it's recommended to set the **Semantic setting to 1** in the "Weight Score".

If business personnel are familiar with the actual questioning scenarios of users and wish to actively adjust the ratio of semantics or keywords, it's recommended to adjust the ratio in the "Weight Score" themselves.

If the content in the knowledge base is complex and cannot be matched by simple conditions such as semantics or keywords, while requiring precise answers, and if you are willing to incur additional costs, it's recommended to use the **Rerank model** for content retrieval.

2. **What should I do if I encounter issues finding the “Weight Score” or the requirement to configure a Rerank model?**

Here's how the knowledge base retrieval method affects Multi-path Retrieval:

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/edaf51316fa078c33deb10cf1273250a.webp" alt=""><figcaption></figcaption></figure>

3. **What should I do if I cannot adjust the “Weight Score” when referencing multiple knowledge bases and an error message appears?**

This issue occurs because the embedding models used in the multiple referenced knowledge bases are inconsistent, prompting this notification to avoid conflicts in retrieval content. It is advisable to set and enable the Rerank model in the "Model Provider" or unify the retrieval settings of the knowledge bases.

4. **Why can't I find the “Weight Score” option in multi-recall mode, and only see the Rerank model?**

Please check whether your knowledge base is using the “Economical” index mode. If so, switch it to the “High Quality” index mode.
