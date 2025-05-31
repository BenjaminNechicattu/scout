import pyautogui

def click_simulation(x, y, duration=0.1):
    """
    Simulates a mouse click at the specified (x, y) coordinates.
    
    :param x: The x-coordinate where the click should occur.
    :param y: The y-coordinate where the click should occur.
    :param duration: The duration of the click in seconds (default is 0.1 seconds).
    """
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()  # Perform the click

def double_click_simulation(x, y, duration=0.1):
    """
    Simulates a double mouse click at the specified (x, y) coordinates.
    
    :param x: The x-coordinate where the double click should occur.
    :param y: The y-coordinate where the double click should occur.
    :param duration: The duration of the double click in seconds (default is 0.1 seconds).
    """
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.doubleClick()  # Perform the double click

def right_click_simulation(x, y, duration=0.1):
    """
    Simulates a right mouse click at the specified (x, y) coordinates.
    
    :param x: The x-coordinate where the right click should occur.
    :param y: The y-coordinate where the right click should occur.
    :param duration: The duration of the right click in seconds (default is 0.1 seconds).
    """
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.rightClick()  # Perform the right click

def drag_simulation(start_x, start_y, end_x, end_y, duration=0.1):
    """
    Simulates a mouse drag from the start coordinates to the end coordinates.
    
    :param start_x: The starting x-coordinate for the drag.
    :param start_y: The starting y-coordinate for the drag.
    :param end_x: The ending x-coordinate for the drag.
    :param end_y: The ending y-coordinate for the drag.
    :param duration: The duration of the drag in seconds (default is 0.1 seconds).
    """
    pyautogui.moveTo(start_x, start_y, duration=duration)
    pyautogui.dragTo(end_x, end_y, duration=duration)  # Perform the drag

def scroll_simulation(x, y, clicks, direction='up', duration=0.1):
    """
    Simulates a mouse scroll at the specified (x, y) coordinates.
    
    :param x: The x-coordinate where the scroll should occur.
    :param y: The y-coordinate where the scroll should occur.
    :param clicks: The number of clicks to scroll (positive for up, negative for down).
    :param direction: The direction of the scroll ('up' or 'down').
    :param duration: The duration of the scroll in seconds (default is 0.1 seconds).
    """
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.scroll(clicks)  # Perform the scroll