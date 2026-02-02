from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

text_splitter=SemanticChunker(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"), breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=3

)

sample='''Autism Spectrum disorder (ASD) is a neurodevelopmental disorder mainly affecting the brain, immune system, and gastrointestinal tract. The redox state of cellular thiols plays an imperative role in maintaining homeostasis
by regulating signal transduction and protein behaviour. 
Cancer results from complex changes across the genome, epigenome, and transcriptome. Its clinical variability shows both distinct subtype structures and ongoing biological gradients. To understand these diOerences, we need integrated methods that combine various data types.'''

docs=text_splitter.create_documents([sample])

print(len(docs))
print(docs)