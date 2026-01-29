from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model_name="gemini-1.5-pro", temperature=0.5) #temperature is the creativity level in which u want ur ans

result=model.invoke('What is the capital of India?')

print(result) #gives many args along with the actual ans
print(result.content) #only the required ans is printed
