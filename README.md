# scout
screen control operator using tools

Aim : Control Personal Computers using voice over interactions.

Architecture : 


```        
Voice commands → Text to speech → LLM → [Image (ss) + Prompt] → Vision Model (e.g. LLaVA)
                                                ↓
                                          execute tool
                            -----------------------------------------
                            |        → pyautogui.click(x, y)        |
                            |        → cli command execution        |
                            |        → keyboard click               |      
                            -----------------------------------------
```


# Getting Started

To set up the project, it is recommended to use a Python virtual environment and install the required packages from `requirements.txt`:

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
-
