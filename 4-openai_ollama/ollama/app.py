import os 
from dotenv import load_dotenv
load_dotenv()

from langchain_community.chat_models import ChatOllama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Langsmith Tracking
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")
os.environ["LANGSMITH_ENDPOINT"]=os.getenv("LANGSMITH_ENDPOINT")

## prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Hey you're a helpful assistant. Please respond to the question asked"),
    ("user", "Question: {question}")
])

## streamlit framework
st.title("Langchain demo with Gemma 2b")
input_text = st.text_input("What question do you have in mind?")

## ollama gemma 2 model
llm = ChatOllama(model = "gemma2:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))