'''
目标：
使用固定阈值、自适应阈值和Otsu阈值法”二值化”图像
OpenCV函数：cv2.threshold(), cv2.adaptiveThreshold()
'''

# 固定阈值分割
import cv2

# 灰度图读入

img = cv2.imread('gradient.jpg', 0)

# 阈值分割
# ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('thresh', th)
# cv2.waitKey(0)

'''
cv2.threshold()用来实现阈值分割，ret是return value缩写，代表当前的阈值，暂时不用理会。函数有4个参数：

参数1：要处理的原图，一般是灰度图
参数2：设定的阈值
参数3：最大阈值，一般为255
参数4：阈值的方式，主要有5种，详情：ThresholdTypes
'''
# 下面结合代码理解下这5种阈值方式：
import matplotlib.pyplot as plt 
 # 应用5中不同的阈值方法

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['original', 'BINARY', 'BINIARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

# 使用matploylib显示
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]),plt.yticks([]) # 隐藏坐标轴

plt.show()