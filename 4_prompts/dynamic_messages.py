from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms , what is {topic}')
])

prompt= chat_template.invoke({'domain':'Scientist', 'topic':'Cell'})

print(prompt)

