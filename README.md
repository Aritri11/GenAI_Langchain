GenAI_Langchain


A structured set of examples covering core concepts of Generative AI using LangChain.
Each top-level directory focuses on one building block (LLMs, chat models, embeddings, prompts, chains, runnables, RAGs, agents) and contains minimal, focused code notebooks/scripts to illustrate that concept in isolation.


Repository structure
text
GenAI_Langchain/
│
├── 1_LLMs/
├── 2_chatmodels/
├── 3_embeddingmodels/
├── 4_prompts/
├── 5_structured_outputs/
├── 6_Chains/
├── 7_Runnables/
├── 8_RAGs/
├── 9_Agents/
└── README.md
1_LLMs
Basic usage of LLM interfaces in LangChain.
​
Typical contents:

Loading different LLM backends (e.g., OpenAI, Hugging Face models).

Simple text completion examples.

Configuration of temperature, max tokens, and other generation parameters.

2_chatmodels
Working with chat-oriented models instead of plain text-completion LLMs.
​
Typical contents:

Creating ChatModel instances.

Using message objects (system, human, AI).

Multi-turn conversations and maintaining chat history.

3_embeddingmodels
Examples for text embeddings.
​
Typical contents:

Creating embedding models.

Converting text to vectors.

Basic similarity search over embeddings.

4_prompts
Everything related to prompt engineering in LangChain.
​
Typical contents:

Prompt templates with variables.

Combining system / user instructions.

Good practices for structured prompts.

5_structured_outputs
Generating structured outputs instead of free-form text.
​
Typical contents:

Using output parsers.

Producing JSON / Pydantic-style objects.

Validating and post‑processing model outputs.

6_Chains
Building chains by composing multiple steps.
​
Typical contents:

Simple LLM chains (prompt → LLM → output).

Sequential and/or branching chains.

Passing intermediate results between steps.

7_Runnables
Using the newer Runnable interfaces for composable workflows.
​
Typical contents:

Converting prompts, models, and tools into Runnable objects.

Piping runnables together (.pipe).

Streaming and parallel execution patterns.

8_RAGs
End‑to‑end Retrieval‑Augmented Generation examples.
​
Typical contents:

Document ingestion and text splitting.

Embeddings + vector stores (FAISS & Chroma).

Retrieval, context construction, and LLM question‑answering.

9_Agents
Examples of agents that use tools and reasoning.
​
Typical contents:

Defining tools and toolkits.

Agent executors that decide which tool to call.

Multi-step reasoning with intermediate tool calls.

Prerequisites
Python 3.x

LangChain and relevant LLM/embedding/vector-store dependencies (OpenAI, local models, etc.).
​

Install typical dependencies with:

bash
pip install -r requirements.txt
(if present; otherwise install langchain and the provider libraries you use).
