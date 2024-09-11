from typing import List
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool("news-search", return_direct=True)
def news_search(query: str) -> str:
    """Use this tool to search for the latest news on a given topic. This is particularly useful for current events or updates on individuals like athletes in competitions."""
    search = DuckDuckGoSearchResults()
    results = search.invoke(query)
    # results = "Neeraj chopra didn't win the gold"
    return str(results)
tools = [news_search]

llm = ChatOllama(
    model="llama3.1:latest",
    temperature=0,
).bind_tools([news_search])

result = llm.invoke(
    "neeraj chopra paris olympics "
)

print(result)
