from langchain.agents import tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_community.tools import DuckDuckGoSearchResults

class SearchInput(BaseModel):
    query: str = Field(description="this has to be a string ")

@tool("search-name", args_schema=SearchInput, return_direct = True)
def find_me(query: str) -> str:
    """simply return my address which is the value below"""
    return "HJ Bhabha hostel"
# print(find_me.name)
# print(find_me.description)
# print(find_me.args)

@tool("news-search", return_direct=True)
def news_search(query: str) -> str:
    """Use this tool to search for the latest news on a given topic. This is particularly useful for current events or updates on individuals like athletes in competitions."""
    search = DuckDuckGoSearchResults()
    results = search.invoke(query)
    # results = "Neeraj chopra didn't win the gold"
    return str(results)
