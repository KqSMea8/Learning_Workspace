# 很多情况下，先阈值后边缘检测，效果会更好
# Canny是用的最多的边缘检测算法

import cv2
import numpy as np 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/handwriting.jpg',0)

_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70) # 滞后阈值

cv2.imshow('canny', np.hstack((img, thresh, edges)))
cv2.waitKey(0)