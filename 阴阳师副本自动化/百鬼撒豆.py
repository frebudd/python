import time
import pywinauto
import win32gui
import random
import win32api
import win32con
import cv2
from PIL import ImageGrab
import os
from 阴阳师副本自动化 import mbpipei

class Baigui:

   def run(self):
       # 连接程序
       app = pywinauto.Application(backend="win32").connect(path="onmyoji.exe")
       time.sleep(3)

       # 获取程序句柄
       hwnd = win32gui.FindWindow(r"Win32Window0", u"阴阳师-网易游戏")
       left, top, right, bot = win32gui.GetWindowRect(hwnd)

       # 点击开始

       sum = 0
       try:
           while sum < 100:
               # 进入按钮
               print("百鬼撒豆次数:" + str(sum))
               time.sleep(random.randint(2, 3))
               randX = random.randint(780, 870)
               randY = random.randint(480, 520)
               win32api.SetCursorPos((left + randX, top + randY))
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

               # 点击选取鬼王
               time.sleep(random.randint(2, 3))
               randPosY = random.randint(350, 450)
               randPosX = random.randint(550, 580)
               win32api.SetCursorPos((left + randPosX, top + randPosY))
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

               # 开始按钮
               time.sleep(random.randint(2, 3))
               brandX = random.randint(1000, 1100)
               brandY = random.randint(520, 610)
               win32api.SetCursorPos((left + brandX, top + brandY))
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

               # 拉条
               time.sleep(random.randint(4, 5))
               drandX = random.randint(340, 350)  # 490 320,340
               drandY = random.randint(610, 620)
               win32api.SetCursorPos((left + drandX, top + drandY))
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
               time.sleep(0.5)
               win32api.SetCursorPos((left + random.randint(500, 690), top + drandY))
               time.sleep(0.5)
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

               # 抓鬼
               count = 0
               while True:
                   template = cv2.imread("fh.png", 0)
                   # time.sleep(random.randint(0, 1) + 0.5)
                   topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
                   if point < 0.04:
                       win32api.SetCursorPos((left + random.randint(100, 1000), top + random.randint(390, 410)))
                       win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                       win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)



                   template = cv2.imread("bgqys.png", 0)
                   topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
                   if point<0.04:
                       # 返回

                       win32api.SetCursorPos((left + random.randint(1100, 1110), top + random.randint(100, 500)))
                       win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                       win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                       break
                   template = cv2.imread("jr.png", 0)
                   topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
                   if point < 0.04:
                       break

                   template = cv2.imread("bgks.png", 0)
                   topLeft, botRight, point = mbpipei.Template(template, left, top, right, bot)
                   if point < 0.04:
                       break






               sum = sum + 1


       except KeyboardInterrupt:
           sys.exit(0)


baig = Baigui()
baig.run()
