from selenium import webdriver



url = "https://www.taobao.com/"
brower = webdriver.Chrome()
brower.get(url)
# print(brower.page_source)
with open("taobao.html", "a", encoding='utf-8')as f:
    f.write(brower.page_source)