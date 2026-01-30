from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model= ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

prompt= template.format()

result=model.invoke(prompt)

final_result=parser.parse(result.content)

# #can also write the above 3 lines as:
# chain= template | model | parser
# result=chain.invoke({})
# print(result)

print(final_result)
#print(final_result['name'])
print(type(final_result))

#json output parser gives the structure of the json as per the model's own decision. It does not allow the user to define the structure