from langchain_huggingface import HuggingFaceEmbeddings
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents= ["Sachin Tendulkar is revered as the “God of Cricket” in India, holding numerous batting records across formats.",
            "MS Dhoni is celebrated for his calm leadership, having captained India to multiple ICC trophies.",
            "Virat Kohli is known for his aggressive mindset and consistency, especially in run-chases.",
            "Kapil Dev led India to its first Cricket World Cup victory in 1983, transforming Indian cricket.",
            "Rohit Sharma is famous for his elegant batting and record-breaking double centuries in ODIs."]

query= 'tell me about rohit sharma'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores= cosine_similarity = cosine_similarity([query_embedding], doc_embedding)[0] #always take the query and the document in the form of 2D list in cosine similarity function [as it was returning a 2D list , to make it 1D -[0] is used]
print(scores)

print(list(enumerate(scores))) #to get the index along with the values so that the indices don't change when sorting is done

print(sorted(list(enumerate(scores)),key=lambda x:x[1])) ##sorting on the basis of the 2nd item, i.e the similarity score in ascending order

print(sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]) #to extract the highest similarity score

index , score =sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("The similarity score is: ", score)











