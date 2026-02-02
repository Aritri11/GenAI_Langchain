from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='C:/Users/Aritri Baidya/Desktop/ML Project/samples_final.csv')

docs=loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)