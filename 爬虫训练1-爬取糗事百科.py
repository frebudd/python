import requests
from bs4 import BeautifulSoup
import tkinter
import wx

class Qsbk:
    url = 'https://www.qiushibaike.com/'
    response = requests.get(url).text
    soup = BeautifulSoup(response)
    contents = soup.select("div.content span")
    authors = soup.select("a h2")
    zan = soup.select("i.number")
    @classmethod
    def out(self):
        items = []
        # after_authors = str(self.authors).replace('<h2>', ' ').replace('</h2>', ' ')
        # after_contents = str(self.contents).replace('<span>', ' ').replace('</span>', ' ').replace('<span class="contentForAll">', ' ').replace('<br/>', '\n')
        # after_zan = str(self.zan).replace('<i class="number">', ' ').replace('</i>', ' ')
        for num in range(0,len(self.authors)):
            item= '作者：%s \n内容：%s赞:%s\n' %(self.authors[num].text,self.contents[num].text,self.zan[num].text)
            items.append(item)
        return items
class myFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'chat',size=(520,450))
        panel=wx.Panel(self)
        labelAll=wx.StaticText(panel,-1,'All Content',pos=(180,0))
        self.text=wx.TextCtrl(panel,-1,size=(480,300),pos=(10,25),style=wx.TE_MULTILINE)
        self.text.SetValue(Qsbk.out()[0])
        self.btnSent=wx.Button(panel,-1,'Next',size=(75,25),pos=(180,360))
        self.Bind(wx.EVT_BUTTON,self.onbtns,self.btnSent)
        self.btnNext = wx.Button(panel, -1, 'Last', size=(75, 25), pos=(280, 360))
        self.Bind(wx.EVT_BUTTON,self.nextbtn,self.btnNext)
    tag = 0
    def onbtns(self, event):
        self.text.SetValue(Qsbk.out()[self.tag+1])
        self.tag += 1
    def nextbtn(self,event):
        self.text.SetValue(Qsbk.out()[self.tag-1])
        self.tag -= 1








app=wx.App()
frame=myFrame()
frame.Show()
app.MainLoop()




