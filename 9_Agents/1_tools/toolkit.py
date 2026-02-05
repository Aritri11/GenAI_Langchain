from langchain_core.tools import tool

#Custom tools
@tool
def multiply(a: int,b: int) -> int:
    """Multiply two numbers"""
    return a*b

@tool
def add(a: int,b: int) -> int:
    """Add two numbers"""
    return a+b

class MathToolkit:
    """
        Lightweight toolkit to expose a collection of math tools.
        `get_tools` returns a list of LangChain Tool objects that can
        be passed directly into an agent or tool-calling chain.
        """
    def get_tools(self):
        # Both `add` and `multiply` are Tool objects (because of @tool)
        # so they have `.name`, `.description`, and JSON schema.
        return [add,multiply]

# Instantiate the toolkit and retrieve the tools
toolkit = MathToolkit()
tools=toolkit.get_tools()

# Inspect tool metadata (what an agent would see)
for tool in tools:
    print(tool.name, "->" , tool.description)