from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model= ChatHuggingFace(llm=llm)

class person(BaseModel):
    name: str = Field(description="Name of person")
    age: int = Field(description="Age of person")
    city: str = Field(description="City the person belongs to")

parser = PydanticOutputParser(pydantic_object=person)

template= PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt= template.invoke({'place':'indian'})
# print(prompt)

result= model.invoke(prompt)

try:
    final_result = parser.parse(result.content)
except Exception:
    import re
    json_text = re.search(r"\{[\s\S]*?\}", result.content).group()
    final_result = person.model_validate_json(json_text)

print(final_result)

#also can be done using chain method
# chain= template | model | parser
#
# final_result=chain.invoke({'place':'indian'})
# print(final_result)