from pynput import keyboard
import datetime
COMBINATIONS=[
    {keyboard.Key.alt_l,keyboard.KeyCode(char='a')},
    {keyboard.Key.alt_l,keyboard.KeyCode(char='A')},
]
current = set()

def execute():
    print("时间:{0};按下 home".format(datetime.datetime.now()))

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
