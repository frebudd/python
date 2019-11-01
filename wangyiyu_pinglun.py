# 搜索网易云上评论超过几万来着
from selenium import webdriver


class Spider:
    page = webdriver.Chrome()
    list_ge = []
    count = 0
    list_url = []
    # first_url = "https://music.163.com/#/song?id=31654747"
    # list_url.append(first_url)
    # print(list_url)
    # 获取歌的地址
    def get_url(self, url= "https://music.163.com/#/song?id=31654747"):
        try:
            self.list_url.append(url)
            self.page.get(url)

            self.page.implicitly_wait(10)
            self.page.switch_to_frame("contentFrame")

            # 判断评论数、获取歌名
            pinglun = self.page.find_element_by_id("cnt_comment_count")
            if int(pinglun.text) > 50000:
                list_ge = []
                ge = self.page.find_element_by_class_name("f-ff2").text
                list_ge.append(ge)

            # 获取歌曲链接
            next_url = self.page.find_elements_by_class_name("s-fc1")[0].get_attribute("href")
            # print("next"+next_url)
            # print("now"+url)

            # 判断如果链接是之前有的就换个链接
            for u in self.list_url:
                if u == next_url:
                    next_url = self.page.find_elements_by_class_name("s-fc1")[1].get_attribute("href")

            # 递归判断、获取5首
            if self.count == 10:
                return 1
            else:
                self.count = self.count+1
                # print(self.count)
                print(url, ge)
                self.get_url(next_url)

        except Exception as e:
            print(e)

    # print(list_url)


spider = Spider()
spider.get_url()





