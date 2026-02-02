from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text= '''class NakliLLM:
    def __init__(self):
        print('LLM created succesfully')

    def predict(self,prompt):
        response_list=[
            'Delhi is the capital of India',
            'Cell is the smallest unit of life',
            'Life is a journey',
            'Machine learning and Deep learning algorithms are becoming famous'
        ]
        return {'response':random.choice(response_list)}
    llm=NakliLLM()
    llm.predict('What is cell?')'''

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)

chunks=splitter.split_text(text)

print(len(chunks))
print(chunks[0])