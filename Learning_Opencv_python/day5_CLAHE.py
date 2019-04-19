'''
自适应均衡化
不难看出来，直方图均衡化是应用于整幅图片的，会有什么问题呢？看下图
'''
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("/home/sanjay/Workspace/learning/Learning_Opencv_python/tsukuba.jpg",0)

equ = cv2.equalizeHist(img)

# plt.subplot(121)
# plt.imshow(img)
# plt.subplot(122)
# plt.imshow(equ)
# plt.show()
'''
很明显，因为全局调整亮度和对比度的原因，脸部太亮，大部分细节都丢失了。

自适应均衡化就是用来解决这一问题的：它在每一个小区域内（默认8×8）进行直方图均衡化。当然，如果有噪点的话，
噪点会被放大，需要对小区域内的对比度进行了限制，所以这个算法全称叫：
对比度受限的自适应直方图均衡化CLAHE(Contrast Limited Adaptive Histogram Equalization)
'''
# 自适应均衡化，参数可选
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('clahe', cl1)

cv2.imshow('equalization', np.hstack((img, equ)))
cv2.waitKey(0)

'''
小结：
直方图是一种分析图像的手段。
cv2.calcHist()和numpy.bincount()均可用来计算直方图，使用Matplotlib绘制直方图。
均衡化用来使图像的直方图分布更加均匀，提升亮度和对比度。
'''