from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda,RunnableBranch


load_dotenv()

prompt1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)


llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task= "text-generation"
)

model= ChatHuggingFace(llm=llm)

parser=StrOutputParser()

report_gen_gen= prompt1| model |parser #this is called LCEL . This is an alternative syntax for RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_gen,branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))