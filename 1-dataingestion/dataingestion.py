# text loader
from langchain_community.document_loaders import TextLoader

loader = TextLoader('1-dataingestion/speech.txt')

text_document = loader.load()
print(text_document)

## reading a pdf file
