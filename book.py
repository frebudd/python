import requests
from bs4 import BeautifulSoup

url="https://www.99lib.net/book/2608/78929.htm"

response = requests.get(url)
# print(response)
content = response.content
print(content)
soup = BeautifulSoup(content)
title = soup.select("h2.h2")
print(title)
articles = soup.select("div#content div")
print(type(articles[0].text))
print(articles[0].text)
# for article in articles:
#     print(article)