import os

isex = os.path.exists("123")
if not isex:
    os.mkdir("123")

with open(r"\123\1.txt", "a", encoding="utf-8") as f:
    f.write("123")