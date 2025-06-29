import threading
import pyautogui
import time
from pynput import keyboard
import sys

target_color = (90, 52, 43)
clicking = False
stop_clicking = False

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

def auto_clicker():
    global stop_clicking, clicking
    x, y = 160, 370
    width, height = 100, 110

    cropped = pyautogui.screenshot(region=(x, y, width, height))
    cropped.save("/Users/quevin.custodio/Desktop/autoclick.png")

    for i in range(100):
        if stop_clicking:
            print("\nClicking stopped")
            break

        pyautogui.click(x=180, y=450)
        print(f"Clicked {i + 1} times", end="\r")

    clicking = False
    stop_clicking = False
    print("\nAuto Click Finished")

def on_key_press(key):
    global clicking, stop_clicking

    try:
        if key.char == "1":
            clicking = True
            threading.Thread(target=auto_clicker).start()
        
        elif key.char == "q":
            print("\nEnded program")
            stop_clicking = True
            return False

    except AttributeError:
        pass
    

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
    1
print("Press '1' to start auto-clicking. Press 'q' to stop and exit.")
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()

# mouse_pos()  # Uncomment to use

# time.sleep(3)
# pyautogui.moveTo(160, 370)
# print("Move cursor")z