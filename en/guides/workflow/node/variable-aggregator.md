# Variable Aggregator

### 1 Definition

Aggregate variables from multiple branches into a single variable to achieve unified configuration for downstream nodes.

The variable aggregation node (formerly the variable assignment node) is a key node in the workflow. It is responsible for integrating the output results from different branches, ensuring that regardless of which branch is executed, its results can be referenced and accessed through a unified variable. This is particularly useful in multi-branch scenarios, as it maps variables with the same function from different branches into a single output variable, avoiding the need for repeated definitions in downstream nodes.

***

### 2 Scenarios

Through variable aggregation, you can aggregate multiple outputs, such as from issue classification or conditional branching, into a single output for use and manipulation by downstream nodes, simplifying data flow management.

**Multi-Branch Aggregation after Issue Classification**

Without variable aggregation, the branches of Classification 1 and Classification 2, after different knowledge base retrievals, would require repeated definitions for downstream LLM and direct response nodes.

<figure><img src="https://assets-docs.dify.ai//img/en/node/764e3268c5401e862da6900a140e6b14.webp" alt=""><figcaption><p>Issue Classification (without Variable Aggregation)</p></figcaption></figure>

By adding variable aggregation, the outputs of the two knowledge retrieval nodes can be aggregated into a single variable.

<figure><img src="https://assets-docs.dify.ai//img/en/node/5f4c6afc8065e239a266eae9e7e92285.webp" alt=""><figcaption><p>Multi-Branch Aggregation after Issue Classification</p></figcaption></figure>

**Multi-Branch Aggregation after IF/ELSE Conditional Branching**

<figure><img src="https://assets-docs.dify.ai//img/en/node/875e89d576d146d50c91fe96989231b5.webp" alt=""><figcaption><p>Multi-Branch Aggregation after Conditional Branching</p></figcaption></figure>

### 3 Format Requirements

The variable aggregator supports aggregating various data types, including strings (`String`), numbers (`Number`), objects (`Object`), and arrays (`Array`).

**The variable aggregator can only aggregate variables of the same data type**. If the first variable added to the variable aggregation node is of the `String` data type, subsequent connections will automatically filter and allow only `String` type variables to be added.

**Aggregation Grouping**

Starting from version v0.6.10, aggregation grouping is supported.

When aggregation grouping is enabled, the variable aggregator can aggregate multiple groups of variables, with each group requiring the same data type for aggregation.
