'''
cv2.copyMakeBorder()用来给图片添加边框，它有下面几个参数：

src：要处理的原图
top, bottom, left, right：上下左右要扩展的像素数
borderType：边框类型，这个就是需要关注的填充方式
其中填充方式有 默认方式和固定值方式最常用
'''
# 固定值填充
'''
cv2.BORDER_CONSTANT这种方式就是边框都填充成一个固定的值，比如下面的程序都填充0:
'''
import cv2
import numpy as np
img = cv2.imread("/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg")
# print(img)

# 固定值边框，统一都填充为0也成为zero padding
cons = cv2.copyMakeBorder(img, 1, 1,1,1, cv2.BORDER_CONSTANT, value=0)
# print(cons)

np_img = np.random.randn(3,3)
# print(np_img)


# 默认边框 cv2.BORDER_DEFAULT其实是取镜像堆成的像素填充
default = cv2.copyMakeBorder(np_img, 1,1,1,1, cv2.BORDER_DEFAULT)
# print(default)

# opencv进行卷积
# 用cv2.filter2D()实现卷积操作

#定义卷积核
kernel = np.ones((3,3), np.float32) / 10

# 卷积操作， -1表示通道数与原图相同
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('conv', dst)
cv2.waitKey(0)