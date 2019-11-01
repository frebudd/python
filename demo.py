import requests
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
data = {
    'name': 'jack',
    'age': 22
}
r = requests.get("http://httpbin.org/get", params=data)
# print(type(r))
# print(r.text)
json_data = r.json()
print(r.json())
# print(type(r.json()))
print('\ufffd')