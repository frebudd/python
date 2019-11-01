import requests
from bs4 import BeautifulSoup
import re
import os


headers = {'user-agent': 'Baiduspider'}
proxies = {
    'http': 'http://122.114.31.177:808'
}
page = requests.get('https://www.zhihu.com/question/299205851/answer/552815493', headers=headers)
# print(page.content)
soup = BeautifulSoup(page.content, features="html.parser")
imgs = soup.select('img')
# imgs = soup.select('img.origin_image.zh-lightbox-thumb.lazy')
imgs.pop(0)

num = 0
isExists = os.path.exists("photo-zhihu2")
if not isExists:
    path = os.mkdir("photo-zhihu2")
    print("在d：创建photo-zhihu文件夹")
for img in imgs:
    if num % 2 != 0:
        r = requests.get(img['src'])
        print(r.content)
        with open(r"D:\untitled2\photo-zhihu2\\" + str(num) + '.jpg', 'wb')as file:
            file.write(r.content)
            print(str(num)+'ok')
    num = num+1