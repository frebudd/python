import requests
from selenium import webdriver
from bs4 import  BeautifulSoup
from selenium.webdriver.common.keys import Keys

#cnt_comment_count 评论数
# srch 搜索框
# print(search_text.id)
# print(search_text.location)
# print(search_text.tag_name)
# view-source:https://music.163.com/song?id=864043623 框架源代码
# https://music.163.com/#/song?id=864043623


brower = webdriver.Chrome()


try:
    url="https://music.163.com/#/song?id=31654747"
    brower.get(url)
    brower.implicitly_wait(10)
    brower.switch_to_frame("contentFrame")
    zan = brower.find_element_by_id("cnt_comment_count")
    print(zan.text)
    # print(brower.page_source)
except Exception as e:
    print(e)


#模拟百度搜索
# brower= webdriver.Chrome()
# try:
#     url = "https://www.baidu.com/"
#     brower.get(url)
#     brower.implicitly_wait(10)
#     search = brower.find_element_by_id("kw")
#     search.send_keys("python")
#     search.send_keys(Keys.ENTER)
#     print(brower.current_url)
#     print(brower.get_cookies())
#     print(brower.page_source)
#
#
# except Exception as e:
#     print(e)
