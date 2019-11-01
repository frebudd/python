import requests

url = "http://placekitten.com/g/500/800"
r = requests.get(url)
with open("cat.jpg", "wb") as f:
    f.write(r.content)