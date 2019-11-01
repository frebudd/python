import time
from PIL import ImageGrab
import cv2
import os
import random
import win32gui, win32api,win32con


def Template(template,left, top, right, bot):
    # 截图
    # time.sleep(random.randint(1, 2))
    # time.sleep(1)
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