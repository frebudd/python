from 阴阳师副本自动化 import mbpipei
import cv2
import win32con, win32api, win32gui
import time
import pywinauto
import random




# 连接程序
app = pywinauto.Application(backend="win32").connect(path="onmyoji.exe")
time.sleep(3)

# 获取程序句柄
hwnd = win32gui.FindWindow(r"Win32Window0", u"阴阳师-网易游戏")
left, top, right, bot = win32gui.GetWindowRect(hwnd)

# 匹配图片
flag=0
while True:

   if flag == 0:

       flag = 1
       # 匹配0星的结界突破
       template = cv2.imread('lx.png', 0)
       topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
       if point < 0.003:
           # print(point)
           mbpipei.myClick(topLeft, botRight, left, top)
           flag = 0

       # 匹配进攻按钮
       template = cv2.imread('jg.png', 0)
       topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
       if point < 0.01:
           mbpipei.myClick(topLeft, botRight, left, top)
           flag = 0

       # # 点击指定式神
       template = cv2.imread("bz.png", 0)
       topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
       # print(point)
       # flag2 = 0
       if point < 0.1 :
           print("heretwo")
           ranX = random.randint(750, 760)
           ranY = random.randint(370, 380)
           win32api.SetCursorPos((left + ranX, top + ranY))
           win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
           win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
           flag = 0
           # flag2 = 1
           time.sleep(20)


       # 点击宝箱
       template = cv2.imread("cb.png", 0)
       topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
       if point < 0.1:
           mbpipei.myClick(topLeft, botRight, left, top)
           flag = 0

       # 点击失败
       template = cv2.imread("sb.png", 0)
       topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
       if point < 0.1:
           mbpipei.myClick(topLeft, botRight, left, top)
           flag = 0

   else:

   # 匹配防守记录，刷新
    template = cv2.imread('sx.png', 0)
    topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
    if point <0.04:
       mbpipei.myClick(topLeft, botRight, left, top)

       # 点击确定
    template = cv2.imread('qd.png', 0)
    topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
    if point <0.04:
       mbpipei.myClick(topLeft, botRight, left, top)

    flag = 0




