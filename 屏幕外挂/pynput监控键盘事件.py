from pynput import keyboard

def on_press(key):
    try:
        print('{0} 按下'.format(key))
    except AttributeError:
        print('{0} 按下'.format(key))

def on_release(key):
    print('{0} 松开'.format(key))

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()