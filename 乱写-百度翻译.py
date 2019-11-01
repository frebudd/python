import requests
# from bs4 import BeautifulSoup
import json



class Spider:
    baseUrl = 'https://fanyi.baidu.com/sug'

    #输入关键字
    def getKW(self, keyword):
        #字典的格式要与response data 一致
        kw = {"kw": keyword}
        # print(url)
        response = requests.post(self.baseUrl, data=kw)
        # content返回的类型是二进制，包括图片文件等等，text返回的是unicode，包括文本
        json_data = response.content.decode('utf-8')
        print(type(json_data))
        # print(json_data)
        # 讲二进制数转为json
        # json_data = json.loads(json_data)
        # 将网页进行jison编译
        json_data = response.json()
        # 输出调试
        print(type(json_data))
        print(json_data['data'][0])


    # def getRes(self,content):
    #     soup=BeautifulSoup(content)
    #     res=soup.select('p')
    #     print(res)




#s实例化
spider = Spider()
keyword = input('please input keyword:')
content = spider.getKW(keyword)
# spider.getRes(content)
