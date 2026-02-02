from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough


load_dotenv()

prompt1= PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Generate a LinkdIn post about- {topic}',
    input_variables=['topic']
)

llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task= "text-generation"
)

model= ChatHuggingFace(llm=llm)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkdin': RunnableSequence(prompt2,model,parser)
})

print(parallel_chain.invoke({'topic':'AI'}))