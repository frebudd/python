import requests
from bs4 import BeautifulSoup
import xlsxwriter


class spider:
    titles=[]
    contents=[]
    prices=[]
    for num in range(1, 21):
        url = "https://cs.lianjia.com/zufang/pg" + str(num) + "/#contentList"
        print("页面" + str(num))

        header = {'user-agent': 'Baiduspider'}
        proxies = {
            'http': 'http://122.114.31.177:808'
        }
        res = requests.get(url, headers=header, proxies=proxies);
        # 页面
        # print(res.text)
        soup = BeautifulSoup(res.text)


        # 标题
        title = soup.select("div.content__list--item--main p.content__list--item--title.twoline")
        # 价格
        price = soup.select("span.content__list--item-price")
        # 内容
        content = soup.select("div.content__list--item--main p.content__list--item--des")
        for num in range(30):
            # print(num)
            titles.append(title[num].text)
            contents.append(content[num].text)
            prices.append(price[num].text)
    # print(contents)
        # 写入excel
    workbook = xlsxwriter.Workbook(r'd:\fangjia.xlsx')
    worksheet = workbook.add_worksheet()
    for num in range(1, 601):
        row = 'A' + str(num)
        row2 = 'B' + str(num)
        row3 = 'C' + str(num)
        worksheet.write_string(row, titles[num - 1])
        worksheet.write_string(row2, contents[num - 1])
        worksheet.write_string(row3, prices[num - 1])
    workbook.close()




Spider = spider();
