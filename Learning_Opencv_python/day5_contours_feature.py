'''
计算物体的周长、面积、质心、最小外接矩形等
OpenCV函数：cv2.contourArea(), cv2.arcLength(), cv2.approxPolyDP() 等
'''
# 先把图片的轮廓找到
import cv2
import numpy as np 

img = cv2.imread("/home/sanjay/Workspace/learning/Learning_Opencv_python/handwriting1.jpg",0)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)


# 以数字3的轮廓为例
cnt = contours[1]

# 为了便于绘制，创建两幅彩色图，并把轮廓画在第一幅图上
img_color1 = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
img_color2 = np.copy(img_color1)
cv2.drawContours(img_color1, [cnt], 0, (0,0,255), 2)

# 轮廓面积
area = cv2.contourArea(cnt)

print(area)

cv2.imshow('contours', np.hstack((img_color1, img_color2)))

# 外接矩形
# 形状的外接矩形有两种，如下图，绿色的叫外接矩形，表示不考虑旋转并且能包含整个轮廓的矩形。蓝色的叫最小外接矩，考虑了旋转
x, y, w, h = cv2.boundingRect(cnt)
# 外接矩形
cv2.rectangle(img_color1, (x, y), (x + w, y + h), (0, 255, 0), 2)
# 最小外接矩形
rect = cv2.minAreaRect(cnt) # 
box = np.int0(cv2.boxPoints(rect))
cv2.drawContours(img_color1, [box], 0, (255, 0,0), 2)

cv2.imshow('contours', np.hstack((img_color1, img_color2)))

cv2.waitKey(0)