'''
大部分图像处理任务都需要先进行二值化操作，阈值的选取很关键，Otsu阈值法会自动计算阈值。

Otsu阈值法（日本人大津展之提出的，也可称大津算法）非常适用于双峰图片，啥意思呢？

双峰图片就是指图片的灰度直方图上有两个峰值，直方图就是每个值（0~255）的像素点个数统计

Otsu算法假设这副图片由前景色和背景色组成，通过统计学方法（最大类间方差）选取一个阈值，
将前景和背景尽可能分开，我们先来看下代码，然后详细说明下算法原理

下面这段代码对比了使用固定阈值和Otsu阈值后的不同结果：

另外，对含噪点的图像，先进行滤波操作效果会更好。
'''
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/noisy.jpg', 0) 

# 固定阈值法
ret1, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# otsu阈值法
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 先进行高斯滤波，再使用Otus阈值法
blur = cv2.GaussianBlur(img, (5,5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 用matplotlib把原图，直方图，和阈值图都显示出来

# images中的0是占位置的，因为第二个可以用plt.hist()
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original', 'Histogram', 'Global(v=100)',
          'Original', 'Histogram', "Otsu's",
          'Gaussian filtered Image', 'Histogram', "Otsu's"]

for i in range(3):
    # 绘制原图
    plt.subplot(3, 3, i * 3 + 1)
    plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3], fontsize=8)
    plt.xticks([]), plt.yticks([])


    # 绘制脂肪图plt.hist, ravel函数将数组降成一维
    plt.subplot(3, 3, i * 3 + 2)
    plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1], fontsize=8)
    plt.xticks([]), plt.yticks([])

    # 绘制阈值图
    plt.subplot(3, 3, i * 3 + 3)
    plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i * 3 + 2], fontsize=8)
    plt.xticks([]), plt.yticks([])

plt.show()