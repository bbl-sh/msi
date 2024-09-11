from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from tools.name import find_me, news_search
from langchain import hub
from dotenv import load_dotenv
load_dotenv()
llm = OllamaLLM(
    model = "llama3.1:latest"
)

input_text = input("Ask me anything : ")
query = input_text

prompt_template = hub.pull("hwchase17/react")
tools =  [news_search]

agent = create_react_agent(llm, tools, prompt_template)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print(agent_executor.invoke({"input": query}))
