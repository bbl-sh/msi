from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import ArxivAPIWrapper

search = DuckDuckGoSearchResults()

# print(search.invoke("Neeraj chopra paris olympics "))
arxiv = ArxivAPIWrapper()
print(arxiv.run("Transformer: Attention is all you need "))
