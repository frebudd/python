import re

content = "hello world  123 what is hanppen  i hate "

r = re.search("hello/sworld",content,re.S)

print(r)