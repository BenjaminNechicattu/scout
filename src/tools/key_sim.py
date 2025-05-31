import keyboard

def simulate_key_press(key):
    """
    Simulate a single key press and release.
    
    Args:
        key (str): The key to press and release (e.g., 'a', 'enter').
    """
    keyboard.press(key)
    keyboard.release(key)

def simulate_key_combination(keys):
    """
    Simulate pressing and releasing a combination of keys.

    Args:
        keys (list of str): The keys to press together (e.g., ['ctrl', 'c']).
    """
    for key in keys:
        keyboard.press(key)
    for key in reversed(keys):
        keyboard.release(key)

