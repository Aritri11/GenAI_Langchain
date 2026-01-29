from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model='gpt-3.5', temperature=0.5) #temperature is the creativity level in which u want ur ans , if the value is kept near to 0 it gives same ans for the given query when increased from 0 it gives different values

result=model.invoke('What is the capital of India?')

print(result) #gives many args along with the actual ans
print(result.content) #only the required ans is printed
