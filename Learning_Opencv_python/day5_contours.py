'''
target:
了解轮廓概念
寻找并绘制轮廓
OpenCV函数：cv2.findContours(), cv2.drawContours()

轮廓是一系列相连的点组成的曲线，代表了物体的基本外形。

谈起轮廓不免想到边缘，它们确实很像。简单的说，轮廓是连续的，边缘并不全都连续（下图）。
其实边缘主要是作为图像的特征使用，比如可以用边缘特征可以区分脸和手，
而轮廓主要用来分析物体的形态，比如物体的周长和面积等，可以说边缘包括轮廓。

寻找轮廓的操作一般用于二值化图，所以通常会使用阈值分割或Canny边缘检测先得到二值图

经验之谈：寻找轮廓是针对白色物体的，一定要保证物体是白色，而背景是黑色，不然很多人在寻找轮廓时会找到图片最外面的一个框。
'''

# 寻找轮廓
# 使用cv2.findContours()寻找轮廓
import cv2
import numpy as np

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/handwriting.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 记得要加INV
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


# 寻找二值化图中的contours
image, contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
'''
参数2：轮廓的查找方式，一般使用cv2.RETR_TREE，表示提取所有的轮廓并建立轮廓间的层级。更多请参考：RetrievalModes
参数3：轮廓的近似方法。比如对于一条直线，我们可以存储该直线的所有像素点，也可以只存储起点和终点。使用cv2.CHAIN_APPROX_SIMPLE就表示用尽可能少的像素点表示轮廓。更多请参考：ContourApproximationModes
简便起见，这两个参数也可以直接用真值3和2表示。
函数有3个返回值，image还是原来的二值化图片，hierarchy是轮廓间的层级关系（番外篇：轮廓层级），这两个暂时不用理会。我们主要看contours，它就是找到的轮廓了，以数组形式存储，记录了每条轮廓的所有像素点的坐标(x,y)。
'''
print(len(contours))
print(contours)

# 轮廓找出来后，为了方便观看，可以像前面图中那样用红色画出来：cv2.drawContours()
cv2.drawContours(img, contours, -1, (0,0,255), 2)
# 其中参数2就是得到的contours，参数3表示要绘制哪一条轮廓，-1表示绘制所有轮廓，参数4是颜色（B/G/R通道，所以(0,0,255)表示红色），参数5是线宽，之前在绘制图形中介绍过
# 经验之谈：很多人画图时明明用了彩色，但没有效果，请检查你是在哪个图上画，画在灰度图和二值图上显然是没有彩色的(⊙o⊙)

cv2.imshow('gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.imshow('contours',  img)
cv2.waitKey(0)