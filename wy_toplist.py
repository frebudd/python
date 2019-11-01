# chrome无头模式
# 循环内不能放创建
# 写入文件换行在内容后加\n



from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time
import os

class Spider:
    # chrome无头模式

    chrome_options = Options()
    chrome_options.add_argument("headless")

    url = "https://music.163.com/#/discover/toplist"
    brower = webdriver.Chrome(chrome_options=chrome_options)
    brower.get(url)
    brower.switch_to_frame("contentFrame")
    # print(brower.page_source)

    def get_list(self):
        try:
            # list = self.brower.find_elements_by_class_name("txt")
            # print(list[1].find_element_by_class_name("a").get_attribute("href"))
            content = BeautifulSoup(self.brower.page_source, features="html.parser")
            list_url = content.select("span.txt a")
            list_title = content.select("span.txt a b")

            num = 0
            list = []
            for i in list_url:
                # 血的教训 创建不能放循环里
                song_url = '"'+"https://music.163.com"+i["href"]+'"'
                song_name = list_title[num]["title"]
                num = num + 1
                song = song_name+":"+song_url
                list.append(song)

            return list

        except Exception as e:
            print(e)

    def save(self, list):
        try:
            isex = os.path.exists("top_list")
            if not isex:
                os.mkdir("top_list")


            name = str(time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())) + ".txt"
            # name = str(time.time()) + ".txt"
            j = 1
            for i in list:
                # with open(r"top_list\"+name, "a", encoding="utf-8") as f:
                #     f.write(i + "\n")
                with open("top_list\\"+name, "a", encoding="utf-8") as f:
                    f.write(i + "\n")
                print("找到第 "+str(j)+" 首:"+i)
                j = j+1
        except Exception as e:
            print(e)


if __name__ == '__main__':
    spider = Spider()
    list1 = spider.get_list()
    spider.save(list1)


