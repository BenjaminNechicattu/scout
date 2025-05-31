import pyautogui

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")
    return "screen.png"