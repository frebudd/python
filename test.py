# photo=[1,2,3,4]
# for num in range(len(photo)):
#     print("{}".format(num+1))
# for i in range(1,6):
#     print(i)

# from selenium import webdriver
# mobile_emulation = {'deviceName': 'iPhone 6'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option("mobileEmulation", mobile_emulation)
# browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
# browser.get("https://m.bilibili.com/video/av61440605.html")

import win32con,win32api,win32gui
import time
# def key_input(self, input_words=''):
#     for word in input_words:
#         win32api.keybd_event(VK_CODE[word], 0, 0, 0)
#         win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)
#         time.sleep(0.1)
#
# key_input(123)

# def key_even(self, input_key):
#     win32api.keybd_event(VK_CODE[input_key], 0, 0, 0)
#     win32api.keybd_event(VK_CODE[input_key], 0, win32con.KEYEVENTF_KEYUP, 0)
#     time.sleep(1)
#
# key_even("space")
# count=0
# while True:
#     time.sleep(1)
#     print(count)
#     count+=1
#     if win32api.keybd_event(13,0,0,0):
#         False
# for i in range(1,10):
#     print(i)
# for i in range(1,50):
#     url = "http://bfo.sdo.com/web4/introduce/prop_list1.asp?page={}&".format(i)
#     print(url)
import os
import threading
# 'D:\zhihu_collection\\' + titles[num].string.replace('/','').replace('?','') + '.html'

# from fake_useragent import UserAgent
#
# ua = UserAgent()
# print(ua.random)
# from PIL import ImageGrab
#
# img = ImageGrab.grab()
# img.show()
# from 阴阳师副本自动化 import 百鬼撒豆 as bg
# # bg.Baigui.run()
# while True:
#     i = input("Enter text (or Enter to quit): ")
#     if not i:
#         break
#     print("Your input:", i)
#     print("While loop has exited")
client_pos =win32gui.ScreenToClient(handle,pos)
tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

# import sys
# import time as T
# import pyautogui
# try:
#     time=0
#     while True:
#         print(time)
#         time+=1
#         T.sleep(1)
#     # pyautogui.click(100,100)
# except KeyboardInterrupt:
#     sys.exit()