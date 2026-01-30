# #without using string_output parsers
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
#
# load_dotenv()
#
# llm=HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task= "text-generation"
# )
#
# model= ChatHuggingFace(llm=llm)
#
# #1st prompt- detailed report
# prompt_template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic'])
#
#
# #2nd prompt- short summary
#
# prompt_template2=PromptTemplate(
#     template='Write a 5 line summary on the following text. \n {text}',
#     input_variables=['text']
# )
#
# prompt1= prompt_template1.invoke({'topic': 'black hole'})
#
# result= model.invoke(prompt1)
#
# prompt2= prompt_template2.invoke({'text':result.content})
#
# result1= model.invoke(prompt2)
#
# print(result1.content)




#with using string output parsers

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model= ChatHuggingFace(llm=llm)

#Detailed report prompt
prompt_template1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"]
)

#Summary prompt
prompt_template2 = PromptTemplate(
    template="Write a 5 line summary of the following text:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt_template1 | model | parser | prompt_template2 | model | parser

result = chain.invoke({"topic": "black hole"})
print(result)

