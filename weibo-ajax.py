from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os

def get_page():
    url='https://weibo.com/u/2940169432?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop'

    chrome_options = Options()
    chrome_options.add_argument('user-agent=Baiduspider')
    chrome_options.add_argument("headless")
    page = webdriver.Chrome(chrome_options=chrome_options)
    page.get(url)
    # print(page.page_source)
    page = BeautifulSoup(page.page_source)
    # div = page.find_elements_by_class_name('WB_feed_detail.clearfix')
    div = page.select(".WB_feed_detail.clearfix")
    imgs = page.select('ul.WB_media_a.WB_media_a_mn.WB_media_a_m6.clearfix li img')

    for img in imgs:
        print(img)
get_page()