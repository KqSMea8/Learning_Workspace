import cv2 
import matplotlib.pyplot as plt 
import numpy as np 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/drawing.jpg')
rows, cols = img.shape[:2]

# 变换前的三个点
pts1 = np.float32([[50, 65], [150, 65], [210, 210]])

# 变换后的三个点
pts2 = np.float32([[50, 100], [150, 65], [100, 250]])

# 生成变换矩阵
# cv2.getAffineTransform()生成变换矩阵，接下来再用cv2.warpAffine()实现变换
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))


plt.subplot(121), plt.imshow(img), plt.title('input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show()
# matplotlib显示是RGB, 然而opencv是以BGR显示，所以颜色会错乱