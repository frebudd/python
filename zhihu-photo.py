import requests
from bs4 import BeautifulSoup
import re
import os


headers = {'user-agent': 'Baiduspider'}
proxies = {
    'http': 'http://122.114.31.177:808'
}
page = requests.get('https://www.zhihu.com/question/309298287/answer/600903980', headers=headers)
# print(page.content)
soup = BeautifulSoup(page.content, features="html.parser")
imgs = soup.select('img')
# imgs = soup.select('img.origin_image.zh-lightbox-thumb.lazy')
imgs.pop(0)

num = 0
isExists = os.path.exists("photo-zhihu")
if not isExists:
    path = os.mkdir("photo-zhihu")
    print("在d：创建photo-zhihu文件夹")
for img in imgs:
    if num % 2 != 0:
        r = requests.get(img['src'])
        print(r.content)
        with open(r"D:\untitled2\photo-zhihu\\" + str(num) + '.jpg', 'wb')as file:
            file.write(r.content)
            print(str(num)+'ok')
    num = num+1
    # r = requests.get(img.attrs['src'])
#     print(r.content)

# 正则表达式图片
# patten = re.compile('https://.*?.jpg')
# items = re.findall(patten, str(imgs))


