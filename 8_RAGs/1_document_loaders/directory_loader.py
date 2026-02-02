from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader= DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs=loader.load() #the 'load()' function loads everything at once, so if there are huge number of input files the process itself gets slower therefore we can use 'lazy load'
docs=loader.lazy_load()

for document in docs:
    print(document.metadata)

# print(len(docs))
#
# print(docs[0].page_content)
#
# print(docs[0].metadata)