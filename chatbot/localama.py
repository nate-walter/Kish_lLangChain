from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

#Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Streamlit Framework
st.title('Langchain Demo first Ollama use case')
input_text=st.text_input("Search the topic you want")

# Ollama LLM
llm = Ollama(model="llama2:latest")

# string parser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
