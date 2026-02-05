from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

# Load environment variables (e.g., OPENAI_API_KEY) from .env
load_dotenv()

# 1. Define a tool that the LLM can call
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    # This is the actual business logic: multiply two integers
    return a * b

# 2. Create an OpenAI chat model
model = ChatOpenAI(
    model="gpt-3.5",
    temperature=0.5,  # 0 = deterministic, 1 = very creative
)

# 3. Bind tools to the model so it knows what it can call
model_with_tool = model.bind_tools([multiply])

# 4. Create the initial user message
query = HumanMessage("can you multiply 3 with 10?")
messages = [query]

# 5. Ask the model; it may decide to call a tool
result = model_with_tool.invoke(messages)
# `result` is an AIMessage; if the model requested a tool, it's in result.tool_calls
messages.append(result)

# 6. Execute the tool the model requested (if any)
# Here we assume there is at least one tool call
tool_call = result.tool_calls[0]          # e.g. {'name': 'multiply', 'args': {'a': 3, 'b': 10}, ...}
tool_result = multiply.invoke(tool_call)  # run multiply(3, 10) behind the scenes

# Add the tool result back into the conversation so the model can see it
messages.append(tool_result)

# 7. Ask the model again to generate a final answer using the tool output
final_response = model_with_tool.invoke(messages)

# Print the final, natural-language answer
print(final_response.content)
