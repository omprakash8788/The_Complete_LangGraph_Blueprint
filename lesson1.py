from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
# Define the state structure 
class HelloWorldState(TypedDict):
    greeting: str # This key will store the greeting message

# Define the node function
def hello_world_node(state:HelloWorldState):
    state["greeting"] = "Hello World, " + state["greeting"]
    return state

# Define the flow of exceution using edges
builder= StateGraph(HelloWorldState)
builder.add_node("greet", hello_world_node)

# Define the flow of execution using edges
builder.add_edge(START, "greet") # Connect START to the "greet" node
builder.add_edge("greet", END) # Connect the "greet" node to END

# Compile and run the graph
graph = builder.compile()
result = graph.invoke({"greeting" : "from LangGraph!"})
print(result)
