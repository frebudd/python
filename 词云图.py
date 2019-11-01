import  jieba
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pylab as plt
import numpy as np


text = open(r"词云卢本伟.txt","r").read()
# print(text)

cutText = jieba.cut(text,cut_all=False)
# print(next(cutText))
ret = " ".join(cutText)


img = plt.imread("卢本伟卡布基诺2.png")
img = np.array(img)

wc = WordCloud(
    font_path=r"simhei.ttf",
    background_color ="white",
    height =350,
    width = 500,
    max_font_size = 50,
    # min_font_size =10,
    mask = img
)
wc.generate(ret)
imgColor = ImageColorGenerator(img)
wc.recolor(color_func=imgColor)
wc.to_file("wordcloud.png")
plt.figure("123")
plt.imshow(wc)
plt.axis("off")
plt.show()