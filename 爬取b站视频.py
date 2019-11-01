import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
# 标签类名里面有空格的用.来代替
# 浏览器移动端模式
# 数据流写入

def getUrl():
    # 宅舞
    # url = "https://www.bilibili.com/v/dance/otaku/?spm_id_from=333.7.b_64616e63655f6f74616b75.3#/all/click/0/1/2019-07-30,2019-08-06"
    # 三次元
    url = "https://www.bilibili.com/v/dance/three_d/?spm_id_from=333.65.b_7072696d6172795f6d656e75.35#/all/click/0/1/2019-07-31,2019-08-07"
    chrome_option = Options()
    chrome_option.add_argument("headless")
    brower = webdriver.Chrome(chrome_options=chrome_option)
    brower.get(url)
    # print(brower.page_source)
    soup = BeautifulSoup(brower.page_source ,features="html.parser")
    videos = soup.select("ul.vd-list.mod-2 li div.spread-module a")
    # 创建视频网址列表
    videoUrl=[]
    for video in videos:
        videoUrl.append("https://m.bilibili.com"+video["href"]+".html")
    return videoUrl



def downloadVideo(videosUrl):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

    # 设置浏览器移动端模式
    mobile_emulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("headless")
    brower = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)

    # 设置视频文件名
    count=1
    for url in videosUrl:
        brower.get(url)
        # 获取VIDEO标签
        soup = BeautifulSoup(brower.page_source, "html.parser")
        video = soup.select("video source")
        videoContent = requests.get("http:" + video[0]["src"], headers=header, stream=True)
        #     创建文件夹
        isExist = os.path.exists("B站视频三次元")
        if not isExist:
            path = os.mkdir("B站视频三次元")
            print("创建文件夹")

        #     下载速度 1024每秒
        chunk_size=1024
        if videoContent.status_code == 200:
            print("success")

            # 写入文件
            with open("B站视频三次元\\B站视频{}.mp4".format(count), "wb") as f:
                for data in videoContent.iter_content(chunk_size=1024):
                    f.write(data)
                    print("视频{}下载中".format(count))
        else:
            print("false")
        count = count + 1



if __name__ == "__main__":
    videoUrl = getUrl()
    downloadVideo(videoUrl)
    print("完成")