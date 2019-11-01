import time
import win32gui, win32ui, win32con, win32api
import pywinauto
from PIL import ImageGrab
import random


# # app = pywinauto.Application(backend="win32").start("notepad.exe").connect(path="notepad").start(r"D:\Onmyoji\Launch.exe")
app = pywinauto.Application(backend="win32").connect(path="onmyoji.exe")
#
time.sleep(3)
#
# dlg = app[r"阴阳师-网易游戏"]

hwnd = win32gui.FindWindow(r"Win32Window0", u"阴阳师-网易游戏")
print(hwnd)
#
#
left, top, right, bot = win32gui.GetWindowRect(hwnd)
# im = ImageGrab.grab(bbox=(left, top, right, bot))
# # im.show()
print(left, top, right, bot)

while True:
    x = random.randint(800, 900)
    y = random.randint(450, 490)
    randTime = random.randint(125, 130)
    randTimeEnd = random.randint(2, 4)
    randPosX = random.randint(900, 1100)
    randPosY = random.randint(350, 600)

    # 点击探索按钮
    win32api.SetCursorPos((left + x, top + y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    time.sleep(randTime)

    win32api.SetCursorPos((left + randPosX, top + randPosY))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    time.sleep(randTimeEnd)
