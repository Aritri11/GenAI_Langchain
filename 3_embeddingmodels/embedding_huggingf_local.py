from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text= "Delhi is the capital of India"

vector= embedding.embed_query(text)

print(str(vector))

#for many queries together
from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document= ["Delhi is the capital of India",
           "Kolkata is the capital if West Bengal",
           "Paris is the capital of France"]

result=embedding.embed_documents(document)

print(str(result))