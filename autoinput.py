from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Spider:
    try:
        page = webdriver.Chrome()
        url = "https://music.163.com/#/song?id=31654747"
        page.get(url)
        search = page.find_element_by_id("srch")
        search.send_keys("aaa")
        search.send_keys(Keys.ENTER)

    except Exception as e:
        print(e)


