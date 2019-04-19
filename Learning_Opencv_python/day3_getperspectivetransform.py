'''
OpenCV中首先根据变换前后的四个点
用cv2.getPerspectiveTransform()生成3×3的变换矩阵，
然后再用cv2.warpPerspective()进行透视变换
'''
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/card.jpg')


# 原图中卡片的四个角点
pts1 = np.float32([[148, 80], [437, 114], [94, 247], [423, 288]])
# 变换后分别在左上、右上、左下、右下四个点
pts2 = np.float32([[0, 0], [320, 0], [0, 178], [320, 178]])


# 生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)
# 进行透视变换，参数3是目标大小
dst = cv2.warpPerspective(img, M, (320, 178))

plt.subplot(121), plt.imshow(img[:,:,::-1]), plt.title('input')
plt.subplot(122), plt.imshow(dst[:,:,::-1]), plt.title('output')
plt.show()