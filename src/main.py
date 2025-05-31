

import os
import signal
import sys
from capture import capture_screen
from utils.ascii import scout_ascii
from utils.utils import graceful_shutdown
from prompts.character import charachter_prompt
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph_ollama import langgraph_ollama

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    os.system("cls" if os.name == "nt" else "clear")
    print(scout_ascii)
    print("S.C.O.U.T : Hi, I am S.C.O.U.T. (Screen Control Operator Using Tools).")

    message_history = [
        SystemMessage(content=charachter_prompt),
    ]

    while True:
        # get user input
        user_input = input("User : ").strip()
        if not user_input:
            continue
        capture_screen()

        message_history.append(HumanMessage(content=user_input))
        # Use LangGraph workflow to get assistant reply
        try:
            result = langgraph_ollama.invoke({"messages": message_history})
            # result["messages"] contains the updated message list
            # The last message is the assistant's reply
            assistant_reply = result["messages"][-1].content
            print(f"S.C.O.U.T : {assistant_reply}")
            message_history = result["messages"]
        except Exception as e:
            print(f"S.C.O.U.T : [Error communicating with Ollama/LangGraph: {e}]")
