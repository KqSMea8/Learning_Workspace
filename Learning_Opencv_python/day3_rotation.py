import numpy as np 
import cv2

# 旋转图片
'''
旋转同平移一样，也是用仿射变换实现的，因此也需要定义一个变换矩阵。
OpenCV直接提供了 cv2.getRotationMatrix2D()函数来生成这个矩阵，该函数有三个参数：

参数1：图片的旋转中心
参数2：旋转角度(正：逆时针，负：顺时针)
参数3：缩放比例，0.5表示缩小一半
'''

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/drawing.jpg')

# img.shape返回行，列，通道数
rows, cols = img.shape[:2]

# 45度旋转图片并缩小一半
M = cv2.getRotationMatrix2D((cols/2, rows/2), -45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("rotaion", dst)
cv2.waitKey(0)


'''
小结：
cv2.resize()缩放图片，可以按指定大小缩放，也可以按比例缩放。
cv2.flip()翻转图片，可以指定水平/垂直/水平垂直翻转三种方式。
平移/旋转是靠仿射变换cv2.warpAffine()实现的。
'''