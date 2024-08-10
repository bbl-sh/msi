from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent

llm = OllamaLLM(
    model = "qwen2:0.5b"
)

messages = [
    ("system", "you are a good ai"),
    ("human", "tell me about {question}")
]

prompts = ChatPromptTemplate.from_messages(messages)

chain = prompts | llm

print(chain.invoke({"question": "What is LangChain?"}))
