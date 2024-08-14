from typing import Annotated
from langchain_ollama.llms import OllamaLLM
from typing_extensions import TypedDict
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
load_dotenv()
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_core.messages import BaseMessage
from tools.name import find_me
from langchain import hub

llm = OllamaFunctions(model="llama3.1")

query = "where am i ?"

prompt_template = hub.pull("hwchase17/react")
tools =  [find_me]

llm_with_tools = llm.bind_tools(tools)

print(llm_with_tools.invoke({"input": query}))
