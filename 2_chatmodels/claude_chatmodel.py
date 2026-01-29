from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model= ChatAnthropic(model_name="claude-sonnet-4-5-20250929", temperature=0.5) #temperature is the creativity level in which u want ur ans

result=model.invoke('What is the capital of India?')

print(result) #gives many args along with the actual ans
print(result.content) #only the required ans is printed
