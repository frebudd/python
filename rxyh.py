from selenium import webdriver
import time
from fake_useragent import UserAgent



'''
先用chrome开一次 getcookie 获取一次cookie，然后线程休息一分钟，输入登录后，再获取cookie，下面直接带入cookie就实现免密登录
brower.quit()可以清理浏览器缓存
'''


# cookie
# brower.add_cookie({'domain': 'joy.sdo.com',
#       'httpOnly': True,
#       'name': 'NSC_CH-Cgp-IE-Iuuq-XIE-80-1',
#       'path': '/',
#       'secure': False,
#       'value': 'ffffffff09884e2945525d5f4f58455e445a4a423660'})
# brower.add_cookie({'domain': '.sdo.com',
#       'httpOnly': True,
#       'name': 'sdo_dw_track',
#       'path': '/',
#       'secure': False,
#       'value': '85NFaRoRmG9HBsJ8GHox7w=='})
# brower.add_cookie({'domain': 'joy.sdo.com',
#       'httpOnly': True,
#       'name': 'ASP.NET_SessionId',
#       'path': '/',
#       'secure': False,
#       'value': 'ti52km45w1yqf055z2t4cj45'})
# brower.add_cookie({'domain': '.sdo.com',
#       'httpOnly': False,
#       'name': 'CAS_LOGIN_STATE',
#       'path': '/',
#       'secure': False,
#       'value': '1'})
# print(brower.get_cookies())

# time.sleep(30)
# print(brower.get_cookies())
class Spider:
    def QD(self):
        try:
            chromeOpiton = webdriver.ChromeOptions()
            # 去掉自动化开头提示
            # chromeOpiton.add_argument('disable-infobars')
            ug = UserAgent().random
            chromeOpiton.add_argument("user_agent="+str(ug))
            chromeOpiton.add_argument("headless")
            brower = webdriver.Chrome(chrome_options=chromeOpiton)

            url = "http://joy.sdo.com/Project/qdh5/Default.aspx"
            brower.delete_all_cookies()
            brower.get(url)

            # 点击签到框
            time.sleep(1)
            el = brower.find_element_by_xpath("./html/body/div[1]/div[3]")
            time.sleep(1)
            el.click()
            time.sleep(1)
            alert = brower.switch_to_alert()
            alert.accept()
            time.sleep(1)
            #     输入账号密码点击登录 点击确定
            brower.switch_to_frame("sdoLoginIframe")
            time.sleep(1)
            elUser = brower.find_element_by_xpath('//*[@id="username"]')
            elUser.send_keys("asdqwe123zcy")

            time.sleep(1)
            elPwrd = brower.find_element_by_xpath('//*[@id="password"]')
            elPwrd.send_keys("a1225977549")

            time.sleep(1)
            elLogin = brower.find_element_by_xpath('//*[@id="btn_user_login"]/span[1]')
            elLogin.click()

            time.sleep(1)
            elSure = brower.find_element_by_xpath('//*[@id="form1"]/div[2]/div[2]')
            elSure.click()
            # 点击签到框
            time.sleep(1)
            el = brower.find_element_by_xpath("./html/body/div[1]/div[3]")
            time.sleep(1)
            el.click()
            # 签到成功图片
            elPic = brower.find_element_by_xpath("/html/body/div[4]/img")
            # 判断元素是否存在
            if elPic.is_displayed():
                print("签到成功")
                return True
            else:
                print("签到失败")
                return False
            brower.quit()
        except Exception as e:
            print(e)

spider = Spider()
spider.QD()