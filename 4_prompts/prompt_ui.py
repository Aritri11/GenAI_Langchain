#static prompt
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# import streamlit as st
# from dotenv import load_dotenv
#
# load_dotenv()
#
# llm=HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task= "text-generation"
# )
#
# model= ChatHuggingFace(llm=llm)
#
# st.header("Research Tool")
#
# user_input= st.text_input("Enter your prompt")
#
# if st.button ("Summarize"):
#     result= model.invoke(user_input)
#     st.write(result.content)
from envs.r_reticulate.Lib.tempfile import template
#static prompts gives a heavy amount of control to the user, which at times leads to hallucinations of the llms

#dyanmic prompts

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task= "text-generation"
)

model= ChatHuggingFace(llm=llm)

st.header("Research Tool")

paper_input= st.selectbox("Select Research Paper Name", ["Attention Is All You Need",
                                                         "BERT: Pre-training of Deep Bidirectional Transformers",
                                                         "GPT-3: Language Models are Few-Shot Learners",
                                                         "Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical","Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)","Medium (3-5 paragraphs)", "Long (detailed explanation)"])

temp = load_prompt('C:/Users/Aritri Baidya/Desktop/MyFiles/Pycharm/Langchain/4_prompts/template.json')

#fill the place
prompt=temp.invoke({'paper_input': paper_input,
                 'style_input': style_input,
                 'length_input': length_input},
                       validate_template=True)
#difference from 'f string'- using this validate_template , whether the no of inputs are correctly given or not that can be checked at the run time itself, reusability of the template

if st.button ("Summarize"):
    result=model.invoke(prompt)
    st.write(result.content)



