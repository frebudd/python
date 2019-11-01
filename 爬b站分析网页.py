import requests
import json



url = "https://cn-gdfs2-cmcc-v-03.acgvideo.com/upgcxcode/74/20/106912074/106912074_nb2-1-30064.m4s?expires=1566731100&platform=pc&ssig=oxhD4AIFzEPcGHyW2vQOcA&oi=1882304752&trid=3522f49f43bc4894885c5818504f14e2u&nfc=1&nfb=maPYqpoel5MI3qOUX6YpRA==&mid=21602784"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/73.0.3683.86 Safari/537.36",
           "Referer:":"https://www.bilibili.com/video/av61469829",
           "Range":"bytes=0-45047954",
           "Origin":"https://www.bilibili.com"}
response = requests.get(url,headers = headers)
print(response.status_code)
