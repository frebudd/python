from PIL import ImageGrab


 
# im = ImageGrab.grab()
# print(im.size)
# im.show()
# # print(imload())
# # box = im.copy()
# box = (100,100,400,400)
# region = im.crop(box)
# region2 = im.crop(box)
# region.show()
# if region == region2:
#     print("true")

# 获取当前剪贴板的照片
# im = ImageGrab.grabclipboard()
# im.show()
bbox = (100,100,200,200)
im = ImageGrab.grab(bbox)
# im.show()
im.save("yys/jietu.png")
