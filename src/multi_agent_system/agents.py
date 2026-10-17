from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .tools import web_search, scrape_url
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

#model setup

llm = ChatGroq(model="openai/gpt-oss-120b", api_key=os.getenv("GROQ_API_KEY"))

#first agent
def biuld_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )

#second agent
def build_reader_agent():
    return create_agent(
        model = llm,
        tools= [scrape_url]
    )

#writer chain

writer_prompt = ChatPromptTemplate