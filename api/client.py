import requests
import streamlit as st

def get_azure_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={"input":{"topic":input_text}})
    
    return response.json()['output']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/short_story/invoke",
                             json={"input":{"topic":input_text}})
    
    return response.json()['output']

st.title("Langchain Demo with LLama2 and AzureOpenAI APIs")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a short story on")

if input_text:
    st.write(get_azure_openai_response(input_text))

if input_text:
    st.write(get_ollama_response(input_text1))