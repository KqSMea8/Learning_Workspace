# 镜像翻转图片，可以用cv2.flip()函数：
# 其中，参数2 = 0：垂直翻转(沿x轴)，参数2 > 0: 水平翻转(沿y轴)，参数2 < 0: 水平垂直翻转

import cv2

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg')

dst1 = cv2.flip(img, 1)
dst2 = cv2.flip(img, 0)
dst3 = cv2.flip(img, -1)

cv2.imshow('horizontal', dst1)
cv2.imshow('vertical', dst2)
cv2.imshow('horizontal&vertical', dst3)

cv2.waitKey(0)