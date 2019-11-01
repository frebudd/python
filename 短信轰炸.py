import requests
import itchat
from threading import Timer



def getNews():
    url = "http://open.iciba.com/dsapi"
    response = requests.get(url)
    content = response.json()["content"]
    note = response.json()["note"]
    translation = response.json()["translation"]
    print(translation)
    return content, note, translation
def sendNews():
    try:
        itchat.login()
        friend = itchat.search_friends(name="filehelper")
        content, note, translation = getNews()
        itchat.send(content, toUserName="filehelper")
        itchat.send(note, toUserName="filehelper")
        itchat.send(translation, toUserName="filehelper")
        Timer(86400, sendNews()).start()
    except:
        data = "error"
        itchat.send(data,toUserName="filehelper")



sendNews()

