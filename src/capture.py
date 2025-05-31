import pyautogui
import io
import base64
import requests
import pyautogui
import io
import base64
import requests
import pyautogui
import io
import base64
import requests

from constants import SCREENSHOT_PATH

def capture_screen(display="left"):
    """
    Capture the screen for a specific display and return a PIL Image object (in-memory).
    display: "left" or "right" (default: "left")
    """
    # Adjust these values for your setup
    # For two 1080p displays side by side:
    # Left: (0, 0, 1920, 1080)
    # Right: (1920, 0, 1920, 1080)
    if display == "left":
        region = (0, 0, 1920, 1080)
    elif display == "right":
        region = (1920, 0, 1920, 1080)
    else:
        region = None  # Full screen fallback
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(SCREENSHOT_PATH)  # Optional: Save to file for debugging
    return screenshot

def analyze_screen_with_llava(
    user_request=None,
    llava_url="http://localhost:11434/api/generate",
    display="left"
):
    """
    Capture the screen, send it to a local LLaVA server, and return the analysis.
    The prompt is structured to request the coordinates of the user-requested portion for clicking.
    """
    # Define display regions
    if display == "left":
        region = (0, 0, 1920, 1080)
        display_desc = "left display (1920x1080, region: x=0-1919, y=0-1079)"
    elif display == "right":
        region = (1920, 0, 1920, 1080)
        display_desc = "right display (1920x1080, region: x=1920-3839, y=0-1079)"
    else:
        region = None
        display_desc = "full virtual desktop"

    system_prompt = (
        f"You are a vision assistant. The screenshot is from the {display_desc}. "
        f"Given a user request, analyze the image and return the (x, y) pixel coordinates (relative to the full virtual desktop) of the requested UI element for clicking. "
        "Respond ONLY with JSON: {\"x\": <number>, \"y\": <number>} and nothing else. "
        "If the element is not found, return {\"x\": null, \"y\": null}."
    )
    if user_request:
        full_prompt = f"{system_prompt}\n\nUser request: {user_request}"
    else:
        full_prompt = f"{system_prompt}\n\nUser request: Find the close button."

    img = capture_screen(display=display)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    img_b64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    payload = {
        "model": "llava",
        "prompt": full_prompt,
        "images": [img_b64],
        "stream": False
    }
    try:
        response = requests.post(llava_url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response") or result
    except Exception as e:
        return f"LLaVA analysis failed: {e}"