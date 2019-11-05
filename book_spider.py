import requests
from bs4 import BeautifulSoup
import os



def get_book(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    text = response.text
    soup = BeautifulSoup(text)
    div_show = soup.select("div.dirShow")[0]
    # print(div_show)
    dirs = div_show.select("li a")
    count = len(dirs)

    for num in range(1, count + 1):
        url = url.replace('0.html', '%s.html').replace('bookDir', 'book')
        url_after = url % (num)
        print(url_after)
        response = requests.get(url_after)
        response.encoding = 'utf-8'
        text = response.text
        soup = BeautifulSoup(text)
        titles = soup.select("table td")
        print(titles[3].text)
        articles = soup.select("div#Content")
        print(articles[0].text)

        # 保存文件
        is_exist = os.path.exists(r"D:\flaskDemo\static\books")
        if not is_exist:
            os.mkdir(r"D:\flaskDemo\static\books")
        title = titles[3].text + ".txt"
        with open(r"D:\flaskDemo\static\books\\" + title, "a", encoding="utf-8") as f:
            f.write(articles[0].text)

if __name__== "__main__":
    # 沉默的大多数
    # url="http://t.icesmall.cn/bookDir/2/335/0.html"
    # 麦田守望者
    # http://t.icesmall.cn/bookDir/1/33/0.html
    # 挪威的森林
    # http://t.icesmall.cn/bookDir/3/423/0.html
    # 输入世界名著网书籍目录地址
    get_book("http://t.icesmall.cn/bookDir/3/423/0.html")