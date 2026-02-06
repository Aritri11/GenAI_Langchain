RAG (Retrieval-Augmented Generation) combines two capabilities:


Information retrieval: finding relevant pieces of external knowledge on demand.



Text generation: using an LLM to answer based on both its internal parameters and the retrieved information.


The 4-step RAG pipeline:
​

Indexing


Retrieval


Augmentation


Generation


Step 1: Indexing:
Indexing is preparing an external knowledge base so it can be searched efficiently at query time. It typically involves:
​

Document ingestion:

Load source content (PDFs, webpages, transcripts, internal docs, etc.) from wherever it lives (servers, Google Drive, S3, etc.) into memory via loaders.
​

Text chunking:

Split large documents into smaller, semantically meaningful chunks so they fit within the model’s context window and support good semantic search (e.g., using recursive character splitters, semantic chunkers, or format-specific splitters).
​

Embedding generation:

Convert each chunk into a dense vector (an embedding) that encodes its meaning, using an embedding model such as OpenAI embeddings or SentenceTransformers.
​

Vector storage:

Store the embeddings (and their original text + metadata) in a vector database (e.g., FAISS, Chroma, Pinecone, Weaviate, Milvus, Qdrant) that will serve as the external knowledge base for RAG.
​

After indexing, you have a vector store that maps from semantic space back to original chunks.

Step 2: Retrieval:
Retrieval is the real-time process of selecting the most relevant chunks from the index for a given user query. It proceeds roughly as:
​

Embed the query:

Use the same embedding model as in indexing to convert the query into a vector in the same space as document embeddings.
​

Semantic search over the vector store:

Find the stored vectors closest to the query vector (e.g., via cosine similarity or approximate nearest neighbors), possibly using more advanced strategies like MMR or contextual compression.
​

Ranking and selection:

Rank candidate chunks by relevance and pick the top few (e.g., top 3–5) to serve as context for answering the query.
​

These selected chunks are the “retrieved context” that the model will rely on.

Step 3: Augmentation (building the prompt with context):
Augmentation is constructing the actual prompt sent to the LLM by combining:
​

The user query

The retrieved context chunks

Optional instructions to control behavior (e.g., “answer only from the context; if insufficient, say you don’t know”).
​

A typical augmented prompt might look like:

System/instruction part: the assistant role and constraints (only use given context, avoid hallucination, say “I don’t know” if needed).
​

Context section: concatenated retrieved chunks (e.g., relevant portions of a lecture transcript explaining gradient descent).
​

Question section: the original user question.
​

This step “augments” the LLM’s parametric knowledge with fresh, task-specific evidence.

Step 4: Generation:
In the final stage, the augmented prompt is fed to the LLM. The model:
​

Reads the injected context plus the question.

Combines that with its internal (parametric) knowledge.

Generates an answer that should stay grounded in the provided context, especially if explicitly instructed to do so.
​

Conceptually, you can view it as: LLM output = f(parametric knowledge + retrieved context + instructions, query).
