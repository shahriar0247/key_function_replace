import keyboard
import time


trigger = "True"
with open("trigger", "w") as f:
        f.write(str(trigger))


def settrigger():
    time.sleep(1 / 10)
    global trigger
    if trigger == "False": 
        trigger = "True"
    else:
        trigger = "False"
    with open("trigger", "w") as f:
        f.write(str(trigger))
    print("trigger set")


keyboard.add_hotkey('shift+caps_lock', lambda: settrigger())


from pynput.keyboard import Key, Controller, Listener

keyboard2 = Controller()

def key_type(keyboard2, keytotype):
    keyboard2.press(Key.backspace)
    keyboard2.release(Key.backspace)
    keyboard2.type(keytotype)

def on_press(key):
    with open("trigger", "r") as f:
        trigger = f.readline()
    print(key)
    if trigger == "True":
        try:
            if key.char == "1":
                key_type(keyboard2,"5")
            elif key.char == "2":
                key_type(keyboard2,"6")
            elif key.char == "7":
                key_type(keyboard2,"-")
            elif key.char == "8":
                key_type(keyboard2,"+")
            elif key.char == "3":
                key_type(keyboard2,"%")
            elif key.char == "4":
                key_type(keyboard2,"^")
            elif key.char == "9":
                key_type(keyboard2,"_")
            elif key.char == "0":
                key_type(keyboard2,"=")
    
              
            
        except:
            pass

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

keyboard.wait('space+1+3')
