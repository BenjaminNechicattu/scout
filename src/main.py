

import os
import signal
import re
from capture import capture_screen, analyze_screen_with_llava
from utils.ascii import scout_ascii
from utils.utils import graceful_shutdown
from prompts.character import charachter_prompt
from tools.click_sim import click_simulation

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph_ollama import langgraph_ollama

# Optionally, import the LLaVA node if you want to use it in a LangGraph chain
# from langgraph_llava import llava_node

def extract_coordinates(response_text):
    match = re.search(r'"x"\s*:\s*(\d+),\s*"y"\s*:\s*(\d+)', response_text)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None

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

        # Analyze the screen with LLaVA and combine with user input
        # vision_result = analyze_screen_with_llava(prompt=f"{user_input.lower()}; Where on the screen should I click? Respond only with JSON: {{\"x\": <number>, \"y\": <number>}}")
        vision_result = analyze_screen_with_llava(user_request=f"{user_input.lower()}")

        # Extract coordinates from the vision result
        coordinates = extract_coordinates(vision_result)
        vision_dicision = ""
        if coordinates:
            x, y = coordinates
            vision_dicision = f"Coordinates for clicking: (x: {x}, y: {y})"
            # Here you can add code to perform the click action using pyautogui
            # pyautogui.click(x, y)

            click_simulation(x, y)  # Assuming you have a function to simulate clicks
        else:
            vision_dicision = "No valid coordinates found in the vision result."
        
        combined_input = f"User said: {user_input}\n\nScreen analysis: {vision_result} \n\n coordinates: {coordinates} \n\n "

        message_history.append(HumanMessage(content=combined_input))
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



