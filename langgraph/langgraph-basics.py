import random
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage


# Define the state structure
class GraphState(TypedDict):
    input: str
    assigned_node: int
    previous_node: str


# Decision-making function for the entry point
def decider(state: GraphState):
    node_num = random.randint(1, 2)
    return dict(input=state['input'],
                assigned_node=node_num,
                previous_node="manager")


# Function for node 1
def node1(state: GraphState):
    return dict(input=state['input'],
                assigned_node=1 if 'node 1' in state['input'] else 2,
                previous_node="node 1")


# Function for node 2
def node2(state: GraphState):
    return dict(input=state['input'],
                assigned_node=2 if 'node 2' in state['input'] else 1,
                previous_node="node 2")


# Decide which node to assign next
def decider_node_assigner(state: GraphState) -> Literal['node 1', 'node 2']:
    assigned_node = state['assigned_node']
    if assigned_node == 1:
        return "node 1"
    else:
        return "node 2"


# Reassignment logic for node 1
def reassign1(state: GraphState) -> Literal['node 2', END]:
    assigned_node = state['assigned_node']
    if assigned_node != 1:
        return "node 2"
    return END


# Reassignment logic for node 2
def reassign2(state: GraphState) -> Literal['node 1', END]:
    if state['previous_node'] == "node 2":
        return END
    return "node 1"


# Create the StateGraph instance
workflow = StateGraph(GraphState)

# Set an entry point
workflow.set_entry_point("decider")

# Add nodes to the graph
workflow.add_node("decider", decider)
workflow.add_node("node 1", node1)
workflow.add_node("node 2", node2)

# Add conditional edges to transition between nodes
workflow.add_conditional_edges("decider", decider_node_assigner)
workflow.add_conditional_edges("node 1", reassign1)
workflow.add_conditional_edges("node 2", reassign2)

# Compile the graph
graph = workflow.compile()

# Example human input message handling
input_message = HumanMessage(content="assign this to node 1")
config = {"configurable": {"thread_id": 6}}

# Run through the graph and print the events
for event in graph.stream({"input": input_message}, config, stream_mode="values"):
    print(event)
