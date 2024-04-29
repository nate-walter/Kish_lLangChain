from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from langchain_openai import AzureOpenAI, AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"

app = FastAPI(
    title="Langchain Server",
    version="0.1.0",
    description="A simple API server"
)

add_routes(
    app,
    AzureOpenAI(deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")),
    path="/azure_openai",
)

# Azure OpenAI LLM
model = AzureOpenAI(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),    
)

llm = Ollama(model="llama2:latest")

prompt_1 = ChatPromptTemplate.from_template("Write me an essay about {topic} in about 100 words.")
prompt_2 = ChatPromptTemplate.from_template("Write me a short story about {topic} in about 100 words.")

add_routes(
    app,
    prompt_1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt_2 | llm,
    path="/short_story"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)