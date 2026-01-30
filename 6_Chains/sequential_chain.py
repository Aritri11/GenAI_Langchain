from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

#Detailed report prompt
prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"]
)

#Summary prompt
prompt2 = PromptTemplate(
    template="Write a 5 line summary of the following text:\n{text}",
    input_variables=["text"]
)


llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task= "text-generation"
)

model= ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser

result= chain.invoke({'topic':'India'})
print(result)