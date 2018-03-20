from pynput.keyboard import Key,Controller
keyboard = Controller()

#按下空格 松开空格
keyboard.press(Key.space)
keyboard.release(Key.space)

keyboard.press('a')
keyboard.release('a')
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')


