from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_classic import hub
from langchain.agents import create_agent
load_dotenv()

#Step1: Initialize the required tools
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
    """
    This functiom fetches the current weather data for a given city
    """
    url=f"https://api.weatherstack.com/current?access_key=6f4fc701f46b9b40232531d7faa4bed7&query={city}"

    response = requests.get(url)
    return response.json()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

#Step 2: Pull the ReAct prompt from LangChain Hub
prompt = hub.pull('hwchase17/react').template #pulls the standard ReAct agent prompt

#Step3: Create the ReAct agent manually with the pulled prompt
agent = create_agent(
    model=model,
    tools=[search_tool,get_weather_data],
    system_prompt=prompt
)

#Step 5: Invoke
response = agent.invoke({'input': 'Find the capital of West Bengal, then find its current weather condition'})
print(response)

#ReAct- design pattern used in AI agents that stands for Reasoning + Acting
#allows LLM to interleave internal reasoning (Thought) with external actions (like tool use) in a structured, multi-step process
#used in multi-step problems, tool-augmented tasks