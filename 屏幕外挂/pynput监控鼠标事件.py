from pynput import mouse

def on_move(x,y):
    print('鼠标移动： {0}'.format((x,y)))

def on_click(x,y,button,pressed):
    print('{0} 在 {1}：{2}:{3}'.format(
        '鼠标左键' if button==mouse.Button.left else '鼠标右键',(x,y),'按下' if pressed else '松开',button
    ))

def on_scroll(x,y,dx,dy):
    print('滚动 {0} at {1}'.format(
        '向下' if dy <0 else '向上',(x,y)
    ))






with mouse.Listener(
    on_move = on_move,
    on_click=on_click,
    on_scroll=on_scroll
) as listener:
    listener.join()