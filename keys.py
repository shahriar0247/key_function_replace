import keyboard
import time

def write (key):
    #time.sleep(1 / 10)
    keyboard.write(key)

keyboard.add_hotkey('ctrl+alt+1', lambda: write("5"))
keyboard.add_hotkey('ctrl+alt+2', lambda: write("6"))
keyboard.add_hotkey('ctrl+alt+9', lambda: write("-"))
keyboard.add_hotkey('ctrl+alt+0', lambda: write("+"))

keyboard.add_hotkey('ctrl+alt+shift+1', lambda: write("%"))
keyboard.add_hotkey('ctrl+alt+shift+2', lambda: write("^"))
keyboard.add_hotkey('ctrl+alt+shift+9', lambda: write("_"))
keyboard.add_hotkey('ctrl+alt+shift+0', lambda: write("="))

keyboard.wait('ctrl+alt+1+3')