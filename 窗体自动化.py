import pywinauto
import time


# app.connect(handle=0x010f0c)
# connect()用于连接已经启动的程序。连接一个已经运行的程序有以下几种方法：
# a)process：进程id
# app = Application().connect(process=2341)
# b)handle：应用程序的窗口句柄
# app = Application().connect(handle=0x010f0c)
# c)path：进程的执行路径（GetModuleFileNameEx 模块会查找进程的每一个路径并与我们传入的路径去做比较）
# app = Application().connect(path=“D:\Office14\EXCEL.exe”)
#
# d)参数组合（传递给pywinauto.findwindows.find_elements()这个函数）
# app = Application().connect(title_re=".*Notepad", class_name=“Notepad”)

# app = pywinauto.Application(backend="win32").start("D:\\Onmyoji\\Launch.exe")
# time.sleep(6)
# app.connect(path="onmyoji")
# app.top_window()
# 开启进程
app = pywinauto.Application(backend="win32").start("notepad.exe")
time.sleep(1)
# 连接进程
app.connect(path="notepad")

# dlg = app[r"记事本"]获取窗口
# dlg.print_control_identifiers()

dlg.menu_select(r"文件->保存")
# edit = dlg[r"Edit"]
# edit.set_text("12345")
# edit.type_keys(r"54321")
dlg2 = app["另存为"]
# edit2 = dlg2[r"Edit"]
# edit2.set_text("123.txt")
dlg2.print_control_identifiers()
# dlg2["保存"].click()
