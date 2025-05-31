from langchain_core.runnables import RunnableLambda
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from capture import analyze_screen_with_llava

def llava_vision_node(state):
    # Get the latest user request from the message history
    user_request = None
    for msg in reversed(state["messages"]):
        if hasattr(msg, "content") and isinstance(msg, HumanMessage):
            user_request = msg.content
            break
    # Analyze the screenshot for the user-requested UI element
    vision_result = analyze_screen_with_llava(user_request=user_request)
    # Add the vision result to the messages (as a system or human message)
    state["messages"].append(SystemMessage(content=f"[Screen Analysis Coordinates]: {vision_result}"))
    return {"messages": state["messages"]}

llava_node = RunnableLambda(llava_vision_node)

# For LangGraph, you can add this node to your graph as needed.
