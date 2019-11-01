import matplotlib.pyplot as plt

xData = ["2000", "2001", "2002", "2003", "2004", "2005"]
yData = [58000, 60200, 63000, 71000, 84000, 90500]
yData2 = [68000, 40200, 53000, 81000, 94000,70500]
ln1, = plt.plot(xData, yData, 'red', linewidth=2.0, linestyle='--', label='first')
ln2, = plt.plot(xData, yData2, 'green', linewidth=3.0, linestyle='-.', label='second')
plt.legend(loc='best')
# x标题 y标题 图像标题 y轴文字代替
plt.xlabel("year")
plt.ylabel("number")
plt.title("test")
plt.yticks([58000, 71000, 99500], [r'simple', r'good', r'best'])
# plt.legend(handles=[ln1, ln2], labels=["first", "second"], loc="lower right")
# 细节 调整
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 71000))
plt.show()