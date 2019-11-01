import tkinter as tk
from 阴阳师副本自动化 import 百鬼撒豆 as bg
import threading



root = tk.Tk()
root.title("yys")
root.geometry("200x300")
root.resizable(width=False, height=False)
btn = tk.Button(root, text="28层副本")
btn.pack()
baigui =bg.Baigui()
p1 = threading.Thread(target=baigui.run)

btn = tk.Button(root, text="百鬼夜行", command=p1.start)
btn.pack()

btn = tk.Button(root ,text="close",command=root.quit)
btn.pack()
root.mainloop()
