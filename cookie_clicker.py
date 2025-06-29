import pyautogui
import time
from pynput import keyboard
import sys

target_color = (90, 52, 43)
clicking = False

def mouse_pos():
    print("Move your mouse around to find the x and y positions")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse position: ({x}, {y})", end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nTracking Stopped")
        return

def auto_clicker(key):
    global clicking
    
    try:
        if key.char == "1" and not clicking:
            clicking = True
            print("\nAuto Click Started")
            x, y = 160, 370
            width, height = 100, 110

            cropped = pyautogui.screenshot(region=(x, y, width, height))
            cropped.save("/Users/quevin.custodio/Desktop/autoclick.png")

            for i in range(100):
                pyautogui.click(x=180, y=450)
                print(f"Clicked {i + 1} times", end="\r")
                time.sleep(0.1)

                if key.char == "q":
                    print("\nExiting program...")
                    return False  # Stops the listener cleanly

            clicking = False
            print("\nAuto Click Finished")


    except AttributeError:
        pass  # Handles non-char keys like shift, etc.

def scanner(target_color, play_sound):
    time.sleep(3)
    screenshot = pyautogui.screenshot()
    screenshot_rgb = screenshot.convert("RGB")

    width, height = screenshot.size
    for x in range(width):
        for y in range(height):
            pixel_color = screenshot_rgb.getpixel((x, y))
            if all(abs(pixel_color[i] - target_color[i]) <= 20 for i in range(3)):
                print(f"Color found at: ({x}, {y})")
                left = max(x - 20, 0)
                top = max(y - 20, 0)
                right = min(x + 130, width)
                bottom = min(y + 60, height)
                cropped_image = screenshot.crop((left, top, right, bottom))
                cropped_image.save("/Users/quevin.custodio/Desktop/cropped.png")
                return
    print("Color not found on screen")

# Start listener
print("Press '1' to auto-click. Press 'q' to quit.")
with keyboard.Listener(on_press=auto_clicker) as listener:
    listener.join()

# mouse_pos()  # Uncomment to use

# time.sleep(3)
# pyautogui.moveTo(160, 370)
# print("Move cursor")