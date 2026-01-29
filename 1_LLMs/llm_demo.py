#To use this we need to buy the API from OpenAI platform
#the API key has to be then stored inside a '.env' file

from langchain_openai import OpenAI
from dotenv import load_dotenv #to load the secret key from the .env file to the current file

load_dotenv() #openAI API key loading

llm = OpenAI(model='gpt-3.5-turbo-instruct') #define the model we want to invoke

result= llm.invoke('What is the capital of India') #the question we want ask the model
print(result)