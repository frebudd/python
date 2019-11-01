import requests
from bs4 import BeautifulSoup
import os

class Spider:
    for i in range(1,7):
        url=""
        if i==1:
            url = "https://www.169tp.com/diannaobizhi/2017/0630/39002.html"
            print("网页"+str(i))
        else:
            url = "https://www.169tp.com/diannaobizhi/2017/0630/39002_{}.html".format(i)
            print("网页"+str(i))
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
        print(url)
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            print("网页获取成功")
        # print(response.content)

        soup = BeautifulSoup(response.content, features="html.parser")
        photos = soup.select("div.big_img p img")
        if len(photos)>0:
            print("图片标签列表获取成功")
        # print(photo)

        # 创建文件夹
        isExist = os.path.exists("日系动漫壁纸")
        if not isExist:
            path = os.mkdir("日系动漫壁纸")
            print("创建文件夹成功")

        # 获取图片路径
        num = 0
        for a in photos:
            print(a["src"])
            photoUrl = a["src"]
            photo = requests.get(photoUrl, headers=headers)
            if photo.status_code==200:
                print("照片地址获取成功")
            else:
                print("照片地址获取失败")
            photoContent = photo.content
            # print(photo)

            #  下载图片
            with open("日系动漫壁纸\\网页{}第{}张.jpg".format(i,num + 1), "wb")as f:
                f.write(photo.content)
                print("图片:{}获取成功".format(num+1))
            num=num+1







spider = Spider()
