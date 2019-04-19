'''
目标：
canny边缘检测的简单概念
opencv函数：cv2.Canny()
'''
import cv2
import numpy as np 

img = cv2.imread("/home/sanjay/Workspace/learning/Learning_Opencv_python/handwriting.jpg", 0)
edges = cv2.Canny(img, 30, 70)

# cv2.imshow('canny', np.hstack((img, edges)))
# cv2.waitKey(0)


# picture gradient
# vertical edge detection

'''
把图片想象成连续函数，因为边缘部分的像素值是与旁边像素明显有区别的，
所以对图片局部求极值，就可以得到整幅图片的边缘信息了。
不过图片是二维的离散函数，导数就变成了差分，这个差分就称为图像的梯度。
'''
# realize sobel egde detection by cv2.filter2D
img1 = cv2.imread("/home/sanjay/Workspace/learning/Learning_Opencv_python/sudoku.jpg", 0)

# define the kernel of vertical detection
kernel = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=np.float32)

dst_v = cv2.filter2D(img1, -1, kernel)

# horizontal detection
dst_h = cv2.filter2D(img1, -1, kernel.T)

cv2.imshow('edge', np.hstack((img1, dst_v, dst_h)))
# cv2.waitKey(0)


# sobel
sobelx = cv2.Sobel(img1, -1, 1, 0, ksize=3) # only x direction
sobely = cv2.Sobel(img1, -1, 0, 1, ksize=3)

cv2.imshow('sobel', np.hstack((img1, sobelx, sobely)))

# 拉普拉斯是二阶导数
laplacian = cv2.Laplacian(img1, -1)

cv2.imshow('laplacian', laplacian)

cv2.waitKey(0)

