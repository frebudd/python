import cv2
import  numpy as np
from matplotlib import pyplot as plt


# 模版匹配
img = cv2.imread("fb.png", 0)
img2 = img.copy()
template = cv2.imread("zdbz.png", 0)
w,h = template.shape[::-1]
method = eval("cv2.TM_CCOEFF")
res = cv2.matchTemplate(img2, template ,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val,max_val,min_loc,max_loc)
topLeft = max_loc
bottomRight = (topLeft[0]+w,topLeft[1]+h)
print(bottomRight)
