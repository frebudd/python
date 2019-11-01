import requests
from bs4 import BeautifulSoup
import json
import random






class Spider:
    baseUrl = "https://tianqi.qq.com/"
    response = requests.get(baseUrl)
    content = response.content.decode("GBK")
    headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection': 'Keep-Alive',
               'Host': 'zhannei.baidu.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    # 代理
    # iplist = ['112.228.161.57:8118', '125.126.164.21:34592', '122.72.18.35:80', '163.125.151.124:9999',
    #           '114.250.25.19:80']
    # proxies = {"http": "http://112.228.161.57:8118", "https": "http://10.10.1.10:1080", }
    # print(content)

    def getPM(self):
        try:
            json_url = "https://wis.qq.com/weather/common?source=pc&weather_type=air%7Crise&province=%E7%" \
                       "A6%8F%E5%BB%BA&city=%E7%A6%8F%E5%B7%9E&callback=jQuery111308663292633070057_153" \
                       "8225857849&_=1538225857855"
            json_data = requests.get(json_url,headers = self.headers)
            json_data = json_data.content.decode("utf-8").strip("jQuery1113019643159425052104_1538062981471").strip(
                "(").strip(")")
            pm = json.loads(json_data).get("data").get("air").get("pm2.5")
            print("PM2.5:"+pm)
            return "PM2.5:"+pm
        except Exception as e:
            print(e)

    #获取温度
    def getTemp(self):
        try:
            json_url = "https://wis.qq.com/weather/common?source=pc&weather_type=observe%7Cforecast_1h%7" \
                       "Cforecast_24h%7Cindex%7Calarm%7Climit%7Ctips%7Crise&province=%E7%A6%8F%E5%BB%BA&" \
                       "city=%E7%A6%8F%E5%B7%9E&county=&callback=jQuery111308663292633070057_1538225857849&_=1538225857854"
            json_data = requests.get(json_url,headers = self.headers)
            json_data = json_data.content.decode("utf-8").strip("jQuery111308170760419225727_1538151639775").strip(
                "(").strip(")")
            temp = json.loads(json_data).get("data").get("observe").get("degree")
            condition = json.loads(json_data).get("data").get("observe").get("weather")
            update = json.loads(json_data).get("data").get("observe").get("update_time")
            print("温度;"+temp+"°C"+"状态:"+condition+" 更新时间:"+update)
            return "温度;"+temp+"°C"+"状态:"+condition+" 更新时间:"+update
        except Exception as e:
            print(e)

    # 获取未来几天的天气
    def getFuture(self):
        try:
            json_url = "https://wis.qq.com/weather/common?source=pc&weather_type=observe%7Cforecast_1h%7C" \
                       "forecast_24h%7Cindex%7Calarm%7Climit%7Ctips%7Crise&province=%E7%A6%8F%E5%BB%BA&" \
                       "city=%E7%A6%8F%E5%B7%9E&county=&callback=jQuery111308663292633070057_1538225857849&_=1538225857854"
            json_data = requests.get(json_url,headers = self.headers)
            json_data = json_data.content.decode("utf-8").strip("jQuery111308170760419225727_1538151639775").strip(
                "(").strip(")")
            future_1_max = json.loads(json_data).get("data").get("forecast_24h").get("2").get("max_degree")
            future_1_min = json.loads(json_data).get("data").get("forecast_24h").get("2").get("min_degree")
            future_1_cdn = json.loads(json_data).get("data").get("forecast_24h").get("2").get("day_weather")

            future_2_max = json.loads(json_data).get("data").get("forecast_24h").get("3").get("max_degree")
            future_2_min = json.loads(json_data).get("data").get("forecast_24h").get("3").get("min_degree")
            future_2_cdn = json.loads(json_data).get("data").get("forecast_24h").get("3").get("day_weather")

            future_3_max = json.loads(json_data).get("data").get("forecast_24h").get("4").get("max_degree")
            future_3_min = json.loads(json_data).get("data").get("forecast_24h").get("4").get("min_degree")
            future_3_cdn = json.loads(json_data).get("data").get("forecast_24h").get("4").get("day_weather")

            future_1 = {"future_1_min": future_1_min, "future_1_max": future_1_max,"condition":future_1_cdn}
            future_2 = {"future_2_min": future_2_min, "future_2_max": future_2_max,"condition":future_2_cdn}
            future_3 = {"future_3_min": future_3_min, "future_3_max": future_3_max,"condition":future_3_cdn}
            future=[]
            future.append(future_1)
            future.append(future_2)
            future.append(future_3)
            return  future
        except Exception as e:
            print(e)

#
# if '__name__' == '__main__':
#     spider = Spider()
#     spider.getPM()
#     spider.getTemp()
#     future = spider.getFuture()
#     print(future)
spider = Spider()
spider.getPM()
spider.getTemp()
future = spider.getFuture()
print(future)