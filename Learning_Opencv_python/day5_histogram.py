'''
计算并绘制直方图
（自适应）直方图均衡化
OpenCV函数：cv2.calcHist(), cv2.equalizeHist()
在计算直方图之前，有几个术语先来了解一下：

dims：要计算的通道数，对于灰度图dims=1，普通彩色图dims=3
range：要计算的像素值范围，一般为[0,256)
bins：子区段数目，如果我们统计0~255每个像素值，bins=256；如果划分区间，比如0~15, 16~31…240~255这样16个区间，bins=16

OpenCV和Numpy中都提供了计算直方图的函数，我们对比下它们的性能。

OpenCV中直方图计算
使用cv2.calcHist(images, channels, mask, histSize, ranges)计算，其中：

参数1：要计算的原图，以方括号的传入，如：[img]
参数2：类似前面提到的dims，灰度图写[0]就行，彩色图B/G/R分别传入[0]/[1]/[2]
参数3：要计算的区域，计算整幅图的话，写None
参数4：前面提到的bins
参数5：前面提到的range
'''
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/hist.jpg',0)
hist = cv2.calcHist([img], [0], None, [256], [0,256])

'''
也可用Numpy的函数计算，其中ravel()函数将二维矩阵展平变成一维数组，之前有提到过：
hist, bins = np.histogram(img.ravel(), 256, [0, 156])

经验之谈：Numpy中还有一种更高效的方式:
hist  = np.bincount(img.ravel(), minlength=256)

绘制直方图
其实Matplotlib自带了一个计算并绘制直方图的功能，不需要用到上面的函数:
'''
plt.hist(img.ravel(), 256, [0, 256])
# plt.show()

'''
当然也可以用前面计算出来的结果绘制：
plt.plot(hist)
plt.show()
'''

'''
从直方图上可以看到图片的大部分区域集中在150偏白的附近，这其实并不是很好的效果，下面我们来看看如何改善它。
一副效果好的图像通常在直方图上的分布比较均匀，直方图均衡化就是用来改善图像的全局亮度和对比度。其实从观感上就可以发现，前面那幅图对比度不高，偏灰白

OpenCV中用cv2.equalizeHist()实现均衡化。我们把两张图片并排显示，对比一下
'''
equ = cv2.equalizeHist(img)

cv2.imshow('equalization', np.hstack((img, equ)))

plt.hist(equ.ravel(), 256, [0, 256])
plt.show()
cv2.waitKey(0)