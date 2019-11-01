import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import codecs
import threading
import time

class Spider:
    chrome_options = Options()
    chrome_options.add_argument("headless")
    brower = webdriver.Chrome(chrome_options=chrome_options)
    for page in range(1, 36):
        brower.get("https://www.zhihu.com/collection/67468386?page="+str(page))

        # print(type(brower.page_source))
        soup = BeautifulSoup(brower.page_source, features="html.parser")
        contents = soup.select("textarea.content")
        titles = soup.select('h2.zm-item-title a')
        # 创建文件夹
        isExists = os.path.exists('D:\zhihu_collection')
        if not isExists:
            path = os.mkdir('D:\zhihu_collection')
            print('创建文件夹成功。')

        for num in range(0, len(contents)):
            try:
                isExist = os.path.exists(
                    'D:\zhihu_collection\\' + titles[num].string.replace('/', '').replace('?', '') + '.html')
                if not isExist:
                    with open('D:\zhihu_collection\\' + titles[num].string.replace('/', '').replace('?', '') + '.html',
                              'a+', encoding='utf-8')as file:
                        file.write(contents[num].string, )
                        print('保存第' + str(page) + '页第' + str(num + 1) + '个收藏问题。')

                # else:
                #     print("已存在")
            except Exception as e:
                print(titles[num].string + '错误'+str(e))
                with open('D:\zhihu_collection\爬取失败.txt', 'a+') as file:
                    file.write(titles[num].string+'\n')
                pass
            continue






# spider = Spider()
p1 = threading.Thread(target=Spider)
# p2 = threading.Thread(target=Spider)
startTime = time.time()
p1.start()
# # p2.start()
p1.join()
# # p2.join()
endTime = time.time()
sumTime = endTime - startTime
print("time cost s:",sumTime)