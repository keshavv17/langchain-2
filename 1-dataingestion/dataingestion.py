# text loader
from langchain_community.document_loaders import TextLoader

loader = TextLoader('1-dataingestion/speech.txt')

text_document = loader.load()
print(text_document,"\n\n")

## reading a pdf file

## web based loader
from langchain_community.document_loaders import WebBaseLoader
import bs4
loader = WebBaseLoader(web_path=("https://lilianweng.github.io/posts/2023-06-23-agent/"),
                       bs_kwargs=dict(parse_only = bs4.SoupStrainer(
                           class_=("post-title", "post-content","post-header")
                       ))
                       )
text_document = loader.load()
print(text_document, "\n\n")

# arxiv

from langchain_community.document_loaders import ArxivLoader
loader = ArxivLoader(
    query="1605.08386",
    load_max_docs=2,
)

docs = loader.load()
print(docs[0].metadata)