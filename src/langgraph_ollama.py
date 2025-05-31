from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.runnables import RunnableLambda
from langchain_community.llms import Ollama

# Set up the LangChain Ollama LLM
ollama_llm = Ollama(model="llama3")

def ollama_llama3(messages):
    # Use LangChain's LLM wrapper for chat
    response = ollama_llm.invoke(messages)
    return response.content if hasattr(response, 'content') else str(response)


# Define a LangGraph node that calls Ollama
ollama_node = RunnableLambda(lambda state: {"messages": state["messages"] + [AIMessage(content=ollama_llama3(state["messages"]))]})

# Define the state schema (a dict with a 'messages' key)
from typing import TypedDict, List
class ChatState(TypedDict):
    messages: List

graph = StateGraph(state_schema=ChatState)
graph.add_node("ollama", ollama_node)
graph.set_entry_point("ollama")
graph.add_edge("ollama", END)
langgraph_ollama = graph.compile()