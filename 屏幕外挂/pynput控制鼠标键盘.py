#控制鼠标
from pynput.mouse import Button,Controller
mouse = Controller()
#定位
mouse.position = (10,20)
#移动
mouse.move(5,-5)
