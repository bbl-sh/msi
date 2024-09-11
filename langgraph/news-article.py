import random
from typing import TypedDict, Literal
from langchain_community.tools.metaphor_search import tool
from langchain_core.prompt_values import ChatPromptValue, ChatPromptValueConcrete
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from langgraph.graph.message import Annotated, Messages, add_messages
import functools

llm = ChatOllama(
    model="llama3.1:latest",
    temperature=0,
)
# Defining the tools
@tool
def news_search(query: str) -> str:
    """You are a news search machine and you will use the tools to do that """
    search = DuckDuckGoSearchResults()
    results = search.invoke("query")
    return results


class State(TypedDict):
    messages: Annotated[list, add_messages]

def create_agent(llm, tools, system_message:str):
    """create react agent"""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "{system_message}"
            ),
            MessagesPlaceholder(variable_name = "messages")
        ]
    )
    prompt = prompt.partial(system_message = system_message)
    if tools:
        return prompt | llm.bind_tools(tools)
    else:
        return prompt | llm

tools = [news_search]

search_template = "Your job is to search web and give me the results "
write_template = "your job is to write the message i give you"

search_agent = create_agent(llm, tools, search_template)

write_agent = create_agent(llm, [], write_template)


def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {
        'messages':[result]
    }
