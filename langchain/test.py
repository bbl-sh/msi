from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from tools.name import find_me
from langchain import hub

llm = OllamaLLM(
    model = "llama3-groq-tool-use:latest"
)

query = "where am i?"

prompt_template = hub.pull("hwchase17/react")
tools =  [find_me]

agent = create_react_agent(llm, tools, prompt_template)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print(agent_executor.invoke({"input": query}))
