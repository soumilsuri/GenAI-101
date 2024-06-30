## instructions to run this in ur system    
## to run this application in ur system download ollama, and use ollama run llama2-uncensored.
## install requirements.txt and use streamlit run locallama.py to run this
## line 9 to line 15 can be removed
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a very helpfull assistant. Answer every query correctly."),
        ("user","Question:{question}")
    ]
) 

# Streamlit framework
st.title("Racist llama 2")
input_txt=st.text_input("Message llama2-uncensored")

# ollama llama2-uncensored 
llm=Ollama(model="llama2-uncensored")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"question":input_txt}))
