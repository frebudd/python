#爬取女生图片



import requests
from bs4 import BeautifulSoup
import os
import shutil


class Spider:

    # 初始化
    def __init__(self):
        self.baseUrl = 'http://www.umei.cc/p/gaoqing/cn/'

    # 获取网页
    def getPage(self,page):
        response = requests.get(self.baseUrl+"%d.htm"%(page))
        # 字符编码
        response.encoding='utf-8'
        contents = response.text
        return contents

    # 获取图片，标题
    def getImg(self,content):
        soup = BeautifulSoup(content, features="html.parser")
        img = soup.select('a.TypeBigPics img')
        # print(len(img))
        # print(img)
        return img
    def getTitle(self,content):

        soup = BeautifulSoup(content, features="html.parser")
        title = soup.select("div.ListTit")
        # print(len(title))
        # print(title)
        return title
    # 创建保存地址
    def mkPath(self):
        isExists = os.path.exists("photo")
        if not isExists:
             path = os.mkdir("photo")
             print("在d：创建photo文件夹")

    # 保存图片
    def dlimg(self, img, title):
        imge = requests.get(img["src"])
        stitle = str(title.text)+".jpg"
        f = open(r"D:\untitled2\photo\\"+stitle, 'wb')
        f.write(imge.content)
        f.close()


# 实例化
spider=Spider()

# spider.dlimg(img[0],title[0])
while True:
    page = int(input("0退出，请输入页数:"))
    if page==0:
        print("已退出")
        break
    else:
        page = spider.getPage(page)
        img = spider.getImg(page)
        title = spider.getTitle(page)
        spider.mkPath()
        for num in range(0, len(img)):
            spider.dlimg(img[num], title[num])
            print("保存第%d照片" % (num))




