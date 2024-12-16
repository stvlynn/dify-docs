# Retrieval Test/Citation

### 1. Retrieval Testing

The Dify Knowledge Base provides a text retrieval testing feature to debug the recall effects under different retrieval methods and parameter configurations. You can enter common user questions in the **Source Text** input box, click **Test**, and view the recall results in the **Recalled Paragraph** section on the right. The **Recent Queries** section allows you to view the history of query records; if the knowledge base is linked to an application, queries triggered from within the application can also be viewed here.

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/0a8eadfd9e7768c1b72069615d90aa4c.webp" alt=""><figcaption><p>Recall Testing</p></figcaption></figure>

Clicking the icon in the upper right corner of the source text input box allows you to change the retrieval method and specific parameters of the current knowledge base. **Changes will only take effect during the recall testing process.** After completing the recall test and confirming changes to the retrieval parameters of the knowledge base, you need to make changes in [Knowledge Base Settings > Retrieval Settings](create-knowledge-and-upload-documents/#id-6-retrieval-settings).

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/02e70c7dc229f012a15aba33f19defa1.webp" alt=""><figcaption><p>Retrieval Settings</p></figcaption></figure>

**Suggested Steps for Recall Testing:**

1. Design and organize test cases/test question sets covering common user questions.
2. Choose an appropriate retrieval strategy: vector search/full-text search/hybrid search. For the pros and cons of different retrieval methods, please refer to the extended reading [Retrieval-Augmented Generation (RAG)](../../learn-more/extended-reading/retrieval-augment/).
3. Debug the number of recall segments (TopK) and the recall score threshold (Score). Choose appropriate parameter combinations based on the application scenario, including the quality of the documents themselves.

**How to Configure TopK Value and Recall Threshold (Score)**

* **TopK represents the maximum number of recall segments when sorted in descending order of similarity scores.** A smaller TopK value will recall fewer segments, which may result in incomplete recall of relevant texts; a larger TopK value will recall more segments, which may result in recalling segments with lower semantic relevance, reducing the quality of LLM responses.
* **The recall threshold (Score) represents the minimum similarity score allowed for recall segments.** A smaller recall score will recall more segments, which may result in recalling less relevant segments; a larger recall score threshold will recall fewer segments, and if too large, may result in missing relevant segments.

***

### 2. Citation and Attribution

When testing the knowledge base effect within the application, you can go to **Workspace -- Add Function -- Citation Attribution** to enable the citation attribution feature.

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/ce727a0267ceaefaf7c0191bf97ea621.webp" alt=""><figcaption><p>Enable Citation and Attribution Feature</p></figcaption></figure>

After enabling the feature, when the large language model responds to a question by citing content from the knowledge base, you can view specific citation paragraph information below the response content, including **original segment text, segment number, matching degree**, etc. Clicking **Link to Knowledge** above the cited segment allows quick access to the segment list in the knowledge base, facilitating developers in debugging and editing.

<figure><img src="https://assets-docs.dify.ai/img/en/knowledge-base/3fa3eea6a68378361fac64927b5f95c6.webp" alt=""><figcaption><p>View Citation Information in Response Content</p></figcaption></figure>
