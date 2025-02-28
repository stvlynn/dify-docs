# End

### 1 Definition

Define the final output content of a workflow. Every workflow needs at least one end node after complete execution to output the final result.

The end node is a termination point in the process; no further nodes can be added after it. In a workflow application, results are only output when the end node is reached. If there are conditional branches in the process, multiple end nodes need to be defined.

The end node must declare one or more output variables, which can reference any upstream node's output variables.

{% hint style="info" %}
End nodes are not supported within Chatflow.
{% endhint %}

***

### 2 Scenarios

In the following [long story generation workflow](iteration.md#example-2-long-article-iterative-generation-another-scheduling-method), the variable `Output` declared by the end node is the output of the upstream code node. This means the workflow will end after the Code node completes execution and will output the execution result of Code.

<figure><img src="https://assets-docs.dify.ai//img/en/node/024e94e3db3b17146b3108e43cdcf6f1.webp" alt=""><figcaption><p>End Node - Long Story Generation Example</p></figcaption></figure>

**Single Path Execution Example:**

<figure><img src="https://assets-docs.dify.ai//img/en/node/80077012f02ea2c1b3bac4faef750f1f.webp" alt=""><figcaption></figcaption></figure>

**Multi-Path Execution Example:**

<figure><img src="https://assets-docs.dify.ai//img/en/node/5c282d022a8dd52568c4ed1f4591217d.webp" alt=""><figcaption></figcaption></figure>
