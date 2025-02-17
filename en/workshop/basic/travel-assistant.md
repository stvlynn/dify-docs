# AI Agent in Practice: Building a Personal Online Travel Assistant

> Author: Steven Lynn. Dify Technical Writer.

In our previous experiment [How to Build an AI Image Generation Application](./build-ai-image-generation-app.md), we gained an initial understanding of the Agent concept and experimented with writing system prompts.

In this experiment, we will continue to explore Agent prompts and learn more structured prompt writing techniques.

### Knowledge Points You Will Master in This Experiment

* Methods for building Agents using Dify
* Structured prompt writing techniques
* How to use variables

### 1. Preparation

Before creating a new Agent, please ensure the following steps are completed:

* Register and log in to [Dify](https://dify.ai). If you want to deploy locally, refer to [Community Version - Docker Compose Deployment](../../getting-started/install-self-hosted/docker-compose.md)
* Configure at least one model provider (Dify provides 200 OpenAI message credits, but it's recommended to configure your own LLM API Key to ensure smooth experimentation)

### 2. Tool Configuration

#### Google

Building an online travel assistant requires using an internet-connected search engine as a reference source. In this article, we'll use Google as an example.

Of course, you can also use other search engines, such as [Bing](https://docs.dify.ai/guides/tools/tool-configuration/bing), or even AI-driven [Perplexity](https://docs.dify.ai/guides/tools/tool-configuration/perplexity).

Dify's Google tool is based on SerpAPI, so you need to first access SerpAPI's API Key management page to apply for an API Key and paste it into the corresponding location in `Dify - Tools`.

The specific steps are as follows:

1. Add SerpAPI API Key:

Visit [SearpAPI - API Key](https://serpapi.com/manage-api-key). If you haven't registered yet, you'll be redirected to the registration page.

SerpAPI provides 100 free API calls per month, which is sufficient for completing this experiment. If you need additional credits, you can add balance or use other open-source solutions.

<figure><img src="https://assets-docs.dify.ai/img/en/basic/007c065c8c90c33458cd6cb968d7fea4.webp" alt=""><figcaption></figcaption></figure>

2. Go to **Dify - Tools - Google**:

Click `Authorize`, enter the API Key, and save.

<figure><img src="https://assets-docs.dify.ai/img/en/basic/40a7a41ad6bb7c790451e35c51f011cc.webp" alt=""><figcaption></figcaption></figure>

#### webscraper

In this experiment, we need a web scraping tool to extract content from specific web pages. Dify provides a built-in tool, so no additional configuration is required.

<figure><img src="https://assets-docs.dify.ai/img/en/basic/9a7febd4fe4be027108ca4dcf2dcbbcf.webp" alt=""><figcaption></figcaption></figure>

#### Wikipedia

We also want the Agent to accurately introduce destination knowledge, and Wikipedia is a good source of knowledge. Dify also has this tool built-in, requiring no additional configuration.

<figure><img src="https://assets-docs.dify.ai/img/en/basic/73e7cb1d53aa4fa8decc767b3f0bebea.webp" alt=""><figcaption></figcaption></figure>

### 3. Building the Agent

First, select `Create Blank Application - Agent`:

Add and enable the tools: `Google`, `webscraper`, and `wikipedia`.

<figure><img src="https://assets-docs.dify.ai/img/en/basic/228dcd40260f67ec7991d71d32e4c38b.webp" alt=""><figcaption></figcaption></figure>

#### Writing Prompts

When writing prompts, we need to use structured prompts to enhance the Agent's task accuracy.

You can use XML to build structured prompts, referring to Claude's article: [Use XML tags to structure your prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags#example-legal-contract-analysis).

Of course, you can also use Markdown to build prompts. There are no strict requirements for prompt writing.

In the following content, we'll demonstrate structured prompt writing methods using the travel assistant as an example.

1. **Role**

**Role** is to define the Agent's identity and professional domain, ensuring its responses meet scenario requirements.

```xml
<role>
You are a professional travel planning AI assistant with the following capabilities:
1. Use `Google Search` for real-time travel information
2. Verify destination cultural background through `Wikipedia`
3. Generate personalized plans based on user budget
4. Output beautiful Markdown format reports in English
</role>
```

2. **Task**

**Task** is to clarify the specific work steps and processes that the Agent needs to complete, guiding the system's standard operating procedures for handling user requests.

```xml
<task>
Please process user requests according to the following workflow:
1. Information Collection:
   - Confirm destination, travel dates, budget range
   - Understand user preferences (culture/nature/food etc.)
   - Inquire about special needs (accessibility/dietary restrictions etc.)

2. Plan Development:
   - Provide 3 hotel options (different price points)
   - Design daily itinerary (including transportation routes)
   - Recommend local unique experiences
   - Suggest essential items checklist

3. Continuous Optimization:
   - Adjust plans based on user feedback
   - Provide backup plans (for weather changes and other contingencies)
</task>
```

3. **Constraints**

**Constraints** are to set the boundary conditions for the Agent's behavior, ensuring the safety, accuracy, and compliance of output content.

```xml
<constraints>
Please strictly follow these limitations:
1. Budget Control: Do not recommend options exceeding user budget by 30%
2. Safety: Avoid areas with recent travel warnings
3. Objectivity: No commercial promotion content
4. Timeliness: Ensure provided information is valid
</constraints>
```

4. **Example Output**

Example output is not a mandatory part. The purpose of example output is to give the Agent a reference format to ensure its output more closely matches our expectations.

Here is the example output for the travel assistant:

```xml
<example_output>

### Detailed Travel Plan

**Hotel Recommendations**
1. The Kensington Hotel (More info: www.doylecollection.com/hotels/the-kensington-hotel)
- Rating: 4.6⭐
- Price: ~$350 per night
- Description: Set in a Regency-style townhouse, this elegant hotel is a 5-minute walk from South Kensington tube station and a 10-minute walk from the Victoria and Albert Museum.

2. The Rembrandt Hotel (More info: www.sarova-rembrandthotel.com)
- Rating: 4.3⭐
- Price: ~$130 per night
- Description: Built in 1911 and originally apartments for Harrods (0.4 miles away), this modern hotel sits opposite the Victoria and Albert Museum, 5 minutes' walk from South Kensington tube station (direct to Heathrow).

**Day 1 - Arrival and Settlement**
- **Morning**: Arrive at the airport. Welcome to your adventure! Our representative will meet you at the airport to ensure a smooth check-in.
- **Afternoon**: Check into the hotel, take some rest to recover energy.
- **Evening**: Take a relaxed walk around the accommodation area to familiarize yourself with the local environment. Discover nearby dining options and enjoy your first pleasant dinner.

**Day 2 - Culture and Nature Tour**
- **Morning**: Start your day at Imperial College, one of the world's top institutions. Enjoy a campus tour.
- **Afternoon**: Choose to visit the Natural History Museum (known for its engaging exhibitions) or the Victoria and Albert Museum (celebrating art and design). Afterward, relax in peaceful Hyde Park, perhaps take a boat ride on the Serpentine.
- **Evening**: Explore local cuisine. We recommend dinner at a traditional British pub.

**Additional Services:**
- **Concierge Service**: During your stay, our concierge service can assist with restaurant reservations, ticket purchases, transportation arrangements, and any special requests to enhance your experience.
- **24/7 Support**: We provide round-the-clock support to address any issues or needs you may encounter during your trip.

Have a great trip, filled with rich experiences and wonderful memories!

</example_output>
```

### Discussion Question 1: How to Standardize User Input?

Usually, our input to the Agent is in natural language, and one drawback of natural language is that it's difficult to standardize. Sometimes it may contain information that the Agent doesn't need or has no value. In this case, we can introduce variables to standardize input.

Dify currently supports several types of variables: `text`, `paragraph`, `dropdown options`, `number`, and `API-based variables`.

In this experiment, selecting the `text` type variable is sufficient.

In **Variables**, by choosing appropriate variable types, we can ask users about their destination, travel duration, and budget.

| Variable Key | Variable Type | Field Name | Required |
| ----------- | ------------- | ---------- | -------- |
| destination | text | Destination | Yes |
| day | text | Travel Duration | Yes |
| budget | text | Travel Budget | Yes |

Note that `Variable Key`, which is the variable name, only supports uppercase and lowercase letters, numbers, and underscores. `Field Name` is the hint content that users can see.

After adding variables, users can provide necessary background information to the application according to the application developer's intent. The effect is as follows:

<figure><img src="https://assets-docs.dify.ai/img/en/basic/87bfdf9d8c326af9d8b229a738466061.webp" alt=""><figcaption></figcaption></figure>
