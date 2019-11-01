import requests
from bs4 import  BeautifulSoup

url = "https://www.iaread.com/book/cate/1"
html=requests.get(url).content.decode("utf- 8")
book = BeautifulSoup(html).select("ul.item li")
print(book[0])