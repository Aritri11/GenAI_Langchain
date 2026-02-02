from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough,RunnableLambda,RunnableBranch


load_dotenv()

prompt= PromptTemplate(
    template='Answer the following question \n {question} from the following text \n {text}',
    input_variables=['question', 'text']
)

llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task= "text-generation"
)

model= ChatHuggingFace(llm=llm)

parser=StrOutputParser()


url='https://www.flipkart.com/motorola-signature-pantone-martini-olive-256-gb/p/itm945fffeb4a94c?pid=MOBHGVJYTCM8BZQF&param=10923&otracker=clp_bannerads_1_5.bannerAdCard.BANNERADS_m_mobile-phones-store_L9P4CZ82V5ZG'

loader=WebBaseLoader(url)

docs=loader.load()

# print(len(docs))
#
# print(docs[0].page_content)
#
# print(docs[0].metadata)

chain = prompt | model |parser

print(chain.invoke({'question':'What is the RAM size?','text':docs[0].page_content}))

