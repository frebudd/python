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
import threading

# 从截图中模版匹配标志按钮
def Template(template):
    # 截图
    # time.sleep(random.randint(1, 2))
    time.sleep(1)
    point = 1
    # while point>0.2:
    bbox = (left, top, right, bot)
    img = ImageGrab.grab(bbox)
    img.save("jietu.png")
    img = cv2.imread("jietu.png", 0)
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
    os.remove("jietu.png")
    point = minVal
    return topLeft,botRight,point

# 点击
def myClick(topLeft,botRight,left, top):
    randX = random.randint(topLeft[0], botRight[0]-20)
    randY = random.randint(topLeft[1], botRight[1]-20)
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

def fuben():
    while True:
        # 点击战斗标志
        template = cv2.imread("zd2.png", 0)
        topLeft, botRight, point = Template(template)
        # 返回相似度判断小于0.2则确定匹配成功
        if point < 0.2:
            myClick(topLeft, botRight, left, top)

            # 点击财宝结束标志
        templateT = cv2.imread("cb.png", 0)
        topLeft, botRight, point = Template(templateT)
        if point < 0.2:
            myClick(topLeft, botRight, left, top)

        # 移动一步
        template = cv2.imread("fh.png", 0)
        topLeft, botRight, point = Template(template)
        # print(1)
        if point < 0.2:
            # print(2)
            template = cv2.imread("zd2.png", 0)
            topLeft, botRight, point = Template(template)
            # 返回相似度判断小于0.2则确定匹配成功
            if point > 0.2:
                # time.sleep(1)
                ranX = random.randint(650, 660)
                ranY = random.randint(450, 460)
                win32api.SetCursorPos((left + ranX + 100, top + ranY))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


        # 点击宝箱
        template = cv2.imread("bx.png", 0)
        topLeft, botRight, point = Template(template)
        if point < 0.1:
            myClick(topLeft, botRight, left, top)
            # 点外面一下
            time.sleep(2)
            ranX = random.randint(650, 660)
            ranY = random.randint(500, 510)
            win32api.SetCursorPos((left + ranX, top + ranY + 150))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            continue
        template = cv2.imread("hdjl.png", 0)
        topLeft, botRight, point = Template(template)
        if point < 0.1:
            ranX = random.randint(650, 660)
            ranY = random.randint(500, 510)
            win32api.SetCursorPos((left + ranX, top + ranY + 150))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        # 匹配层副本
        template = cv2.imread("16.png", 0)
        topLeft, botRight, point = Template(template)
        if point < 0.04:
            myClick(topLeft, botRight, left, top)
        # 匹配点击探索按钮,点击探索按钮
        template = cv2.imread("ts.png", 0)
        topLeft, botRight, point = Template(template)
        if point < 0.04:
            myClick(topLeft, botRight, left, top)
            # print("探索次数:", myTime)
            # myTime = myTime + 1




p1 = threading.Thread(target=fuben())
p2 = threading.Thread(target=fuben())
p1.start()
p2.start()


