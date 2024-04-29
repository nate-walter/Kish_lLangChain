from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import AzureOpenAI, AzureOpenAIEmbeddings

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
st.title('Langchain Demo With Azure OpenAI API')
input_text=st.text_input("Search the topic you want")


# Azure OpenAI LLM
llm = AzureOpenAI(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),    
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))