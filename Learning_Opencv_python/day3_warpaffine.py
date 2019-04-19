'''
平移是用仿射变换函数cv2.warpAffine()实现的：
'''

# 平移图片
import numpy as np 
import cv2

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/drawing.jpg')

# img.shape返回行，列，通道数
rows, cols = img.shape[:2]

# 定义平移矩阵，需要的是numpy的float32类型
# x 轴平移100， y轴平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 用仿射变换实现平移
dst = cv2.warpAffine(img, M, (cols, rows)) # 这里的dsize应该是要指定(width, height)

cv2.imshow('shift', dst)
cv2.waitKey(0)