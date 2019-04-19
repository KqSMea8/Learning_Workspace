'''
实现旋转、平移和缩放图片
OpenCV函数：cv2.resize(), cv2.flip(), cv2.warpAffine()
affine:仿射变换

图像的几何变换从原理上看主要包括两种：
基于2×3矩阵的仿射变换（平移、缩放、旋转和翻转等）、基于3×3矩阵的透视变换
'''
# 缩放图片
# 缩放就是调整图片的大小，使用cv2.resize()函数实现缩放。可以按照比例缩放，也可以按照指定的大小缩放
import cv2

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/drawing.jpg')

# 按照制定的宽度、高度缩放图片
res = cv2.resize(img, (132, 150))

# 按照比例缩放，如x，y轴均放大一倍
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('shrink', res), cv2.imshow('zoom', res2)
cv2.waitKey(0)