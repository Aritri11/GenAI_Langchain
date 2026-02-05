# Imports
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import requests
from typing import Annotated
from langchain_core.tools import InjectedToolArg
import json

load_dotenv()

# --------------------------------------------------------------------
# Tool 1: Fetch currency conversion factor from an external REST API
# --------------------------------------------------------------------
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    Fetch the currency conversion factor between a given base currency and a target currency.
    For example, USD -> INR.
    """
    # Build the API endpoint URL dynamically from base and target currencies
    url = (
        f"https://v6.exchangerate-api.com/v6/3ad6c735744d07f662d490fd/"
        f"pair/{base_currency}/{target_currency}"
    )

    # Make the HTTP GET request to the currency API
    response = requests.get(url)

    # Return the parsed JSON payload (contains conversion_rate, etc.)

    return response.json()

# Example direct manual call (bypassing the model)
# print(get_conversion_factor.invoke({'base_currency': "USD", 'target_currency': "INR"}))

# --------------------------------------------------------------------
# Tool 2: Convert a base amount using a conversion rate
# --------------------------------------------------------------------
@tool
def convert(
    base_currency_value: int,
    conversion_rate: Annotated[float, InjectedToolArg],
) -> float:
    """
    Given a currency conversion rate, calculate the target currency value
    from a given base currency value.
    """
    # Simple arithmetic: amount * rate
    return base_currency_value * conversion_rate

# Inspect tool schema if desired
# print(convert.args)

# --------------------------------------------------------------------
# Bind tools to an OpenAI chat model
# --------------------------------------------------------------------

# Create a ChatOpenAI model (model name and API key taken from env)
llm = ChatOpenAI()

# Attach both tools so the model can call them
llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

# --------------------------------------------------------------------
# Step 1: User asks a question that implies using both tools
# --------------------------------------------------------------------
messages = [
    HumanMessage(
        "What is the conversion factor between USD and INR, "
        "and based on that can you convert 10 usd to inr?"
    )
]

# --------------------------------------------------------------------
# Step 2: Ask the model; it will decide which tools to call
# --------------------------------------------------------------------
ai_message = llm_with_tools.invoke(messages)

# Append the AI's tool-calling plan/response to the conversation
messages.append(ai_message)

# Debug: see which tool calls the model requested
# print(ai_message.tool_calls)

# --------------------------------------------------------------------
# Step 3: Execute the tools requested by the model
# --------------------------------------------------------------------
for tool_call in ai_message.tool_calls:
    # If the model requested the FX rate:
    if tool_call["name"] == "get_conversion_factor":
        # Execute get_conversion_factor based on the tool_call payload
        tool_message1 = get_conversion_factor.invoke(tool_call)

        # Parse the JSON string content to extract the numeric conversion_rate
        conversion_rate = json.loads(tool_message1.content)["conversion_rate"]

        # Add the tool result message to the conversation history
        messages.append(tool_message1)

    # If the model requested the conversion calculation:
    if tool_call["name"] == "convert":
        # Read whatever the model provided as the conversion_rate argument
        conversion_rate = tool_call["args"]["conversion_rate"]

        # Execute the conversion tool
        tool_message2 = convert.invoke(tool_call)

        # Add this tool result message to the conversation
        messages.append(tool_message2)

# --------------------------------------------------------------------
# Step 4: Ask the model again to explain the result in natural language
# --------------------------------------------------------------------
final_response = llm_with_tools.invoke(messages)

# Print final LLM answer, which should reference both the rate and the amount
print(final_response.content)
