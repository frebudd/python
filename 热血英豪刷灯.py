import win32api
import win32con
import time
import random
import pywinauto
import win32gui

# 三秒钟弹到界面
time.sleep(3)
while True:
    # 按a键
    time.sleep(random.randint(1,2))
    win32api.keybd_event(65, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(65, 0,win32con.KEYEVENTF_KEYUP, 0)
    # 按F5键
    win32api.keybd_event(116, 0, 0, 0)
    time.sleep(1)
    win32api.keybd_event(116, 0, win32con.KEYEVENTF_KEYUP, 0)



#     # 连接程序
#     app = pywinauto.Application(backend="win32").connect(path="amped.exe")
#     time.sleep(3)
#
#     # 获取程序句柄
#     hwnd = win32gui.FindWindow(r"runtimetest_win", u"新热血英豪")
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#
    # # 双击人物
    # time.sleep(random.randint(1,2))a
    # win32api.SetCursorPos((left+random.randint(30,90),top+random.randint(100,150)))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    # time.sleep(0.5)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)


#
#
# #     点击神灯
#     time.sleep(random.randint(2,3))
#     win32api.SetCursorPos((left+random.randint(205,220),top+random.randint(570,575)))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
#     time.sleep(0.5)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#
# #     开启神灯
#     time.sleep(random.randint(1,2))
#     win32api.SetCursorPos((left+random.randint(330,360),top+random.randint(470,480)))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
#     time.sleep(0.5)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

