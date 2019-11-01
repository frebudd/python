import time
import pywinauto
import win32gui
import random
import win32api
import win32con
from PIL import ImageGrab
import cv2
import  numpy as np
from matplotlib import pyplot as plt
import os

# 从截图中模版匹配标志按钮
def Template(template,img):
    # 截图
    time.sleep(random.randint(1, 2))
    point = 1
    # while point>0.2:
    # img = cv2.imread("fb.png",0)
    w, h = template.shape[::-1]
    method = eval("cv2.TM_SQDIFF_NORMED")
    res = cv2.matchTemplate(img, template, method)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
    topLeft = minLoc
    botRight = (topLeft[0] + w, topLeft[1] + h)
    # 画图
    # cv2.rectangle(img, topLeft, botRight, 255, 2)
    # plt.subplot(224), plt.imshow(img, cmap="gray")
    # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.show()

    point = minVal
    return topLeft,botRight,point

# 点击
def myClick(topLeft,botRight,left, top):
    randX = random.randint(topLeft[0], botRight[0]-30)
    randY = random.randint(topLeft[1], botRight[1]-30)
    # print(topLeft[0], botRight[0],topLeft[1], botRight[1],randX, randY)
    win32api.SetCursorPos((left+randX, top+randY))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(random.randint(1, 2))
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)



# 连接程序
app = pywinauto.Application(backend="win32").connect(path="onmyoji.exe")
time.sleep(3)

hwnd = win32gui.FindWindow(r"Win32Window0", u"阴阳师-网易游戏")
left, top, right, bot = win32gui.GetWindowRect(hwnd)
myTime=1
while True:
    bbox = (left, top, right, bot)
    img = ImageGrab.grab(bbox)
    img.save("jietu.png")
    img = cv2.imread("jietu.png", 0)
    # 点击战斗标志
    template = cv2.imread("zd2.png", 0)
    topLeft, botRight, point = Template(template, img)
    # 返回相似度判断小于0.2则确定匹配成功
    if point < 0.2:
        myClick(topLeft, botRight, left, top)

        # 点击财宝结束标志
    templateT = cv2.imread("cb.png", 0)
    topLeft, botRight, point = Template(templateT, img)
    if point < 0.2:
        myClick(topLeft, botRight, left, top)
        # 移动一步
        time.sleep(1)
        ranX = random.randint(650, 660)
        ranY = random.randint(450, 460)
        win32api.SetCursorPos((left + ranX + 100, top + ranY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # 点击宝箱
    template = cv2.imread("bx.png", 0)
    topLeft, botRight, point = Template(template,img)
    if point < 0.1:
        myClick(topLeft, botRight, left, top)
        # 点外面一下
        time.sleep(1)
        ranX = random.randint(650, 660)
        ranY = random.randint(450, 460)
        win32api.SetCursorPos((left + ranX, top + ranY + 100))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        continue

    # 匹配2层副本
    template = cv2.imread("2.png", 0)
    topLeft, botRight, point = Template(template,img)
    if point<0.04:
        myClick(topLeft, botRight, left, top)
    # 匹配点击探索按钮,点击探索按钮
    template = cv2.imread("ts.png", 0)
    topLeft, botRight, point = Template(template,img)
    if point<0.04:
        myClick(topLeft, botRight, left, top)
        print("探索次数:",myTime)
        myTime=myTime+1
    os.remove("jietu.png")


