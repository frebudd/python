import requests
from bs4 import BeautifulSoup


class BDTB:
    def __init__(self):
        self.url='http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'

    def getContent(self,page):
        self.url='http://tieba.baidu.com/p/3138733512?see_lz=1'+'&pn='+str(page)
        text = requests.get(self.url).text
        soup=BeautifulSoup(text)
        div1=soup.select('div.d_post_content.j_d_post_content')
        print(self.url)
        for each in div1:
            print('%s\n----------------------------------------------------------------------------------------------------------------'
                  '------------------------------------\n\n\n'%(each.text))


bdtb=BDTB()
while 1:
    page=input('请输入页数,0退出')
    if page==0:
        break
    else:
        bdtb.getContent(page)



