from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda,RunnableBranch


load_dotenv()

prompt= PromptTemplate(
    template='Write a summary for the following poem- \n {poem}',
    input_variables=['poem']
)

llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task= "text-generation"
)

model= ChatHuggingFace(llm=llm)

parser=StrOutputParser()

loader=TextLoader('C:/Users/Aritri Baidya/Desktop/MyFiles/Pycharm/Langchain/8_RAGs/1_doc_loaders/poem_doc', encoding='utf-8')

docs= loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model |parser

print(chain.invoke({'poem':docs[0].page_content}))






















