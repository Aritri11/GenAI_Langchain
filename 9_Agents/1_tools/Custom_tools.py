#1. Simple tool creation using @tool decorator

from langchain_core.tools import tool

#Step 1: create a function
def multiply(a,b):
    """Multiply two numbers"""
    return a*b

#Step 2: Add type hints

def multiply(a: int,b: int) -> int:
    """Multiply two numbers"""
    return a*b

#Step 3: Add tool decorator
@tool
def multiply(a: int,b: int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({'a':6, 'b':8})
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

#what a llm sees:
print(multiply.args_schema.model_json_schema())

#2. Simple tool creation using Structured Tool

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(description="The first number to add")
    b: int = Field(description="The second number to add")


def multiply_func(a: int, b: int) -> int:
    return a*b

multiply_tool=StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput
)

result=multiply_tool.invoke({'a':6, 'b':8})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)


#3. Simple tool creation using Base Tool

from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

#arg schema using pydantic
class MultiplyInput(BaseModel):
    a: int = Field(description="The first number to add")
    b: int = Field(description="The second number to add")

class MultiplyTool(BaseTool):
    name: str="multiply"
    description: str="Multiply two numbers"

    # type annotation + value are separate
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a*b

multiply_tool=MultiplyTool()

result = multiply_tool.invoke({'a':6, 'b':8})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)