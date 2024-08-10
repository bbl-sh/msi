from langchain.agents import tool
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool

class SearchInput(BaseModel):
    query: str = Field(description="this has to be a string ")

@tool("search-name", args_schema=SearchInput, return_direct = True)
def find_me(query: str) -> str:
    """simply return my address which is the value below"""
    return "HJ Bhabha hostel"
