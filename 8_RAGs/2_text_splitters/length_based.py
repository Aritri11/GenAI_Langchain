from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('C:/Users/Aritri Baidya/Desktop/MyFiles/Pycharm/Langchain/8_RAGs/1_doc_loaders/Aritri_Manuscript.pdf')

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0, #helps to maintain context between two chunks. With increase in chunk_size this should also be increased
    separator=' '
)

result=splitter.split_documents(docs) #split_text is used when simple text is present

#print(result)

print(result[0].page_content) #page_content of 1st chunk bcz of '[0]'
