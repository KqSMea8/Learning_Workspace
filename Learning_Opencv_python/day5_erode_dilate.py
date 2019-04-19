'''
了解形态学操作的概念
学习膨胀、腐蚀、开运算和闭运算等形态学操作
OpenCV函数：cv2.erode(), cv2.dilate(), cv2.morphologyEx()

形态学操作其实就是改变物体的形状，比如腐蚀就是”变瘦”，膨胀就是”变胖”

经验之谈：形态学操作一般作用于二值化图，来连接相邻的元素或分离成独立的元素。腐蚀和膨胀是针对图片中的白色部分！

'''

# 腐蚀
# 腐蚀的效果是把图片”变瘦”，其原理是在原图的小区域内取局部最小值。因为是二值化图，只有0和255，所以小区域内有一个是0该像素点就为0：
# OpenCV中用cv2.erode()函数进行腐蚀，只需要指定核的大小就行
import cv2
import numpy as np 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/j.bmp',0)
# 这个核也叫结构元素，因为形态学操作其实也是应用卷积来实现的。结构元素可以是矩形/椭圆/十字形，可以用cv2.getStructuringElement()来生成不同形状的结构元素，比如
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆结构
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字形结构
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel)


# 膨胀
# 膨胀与腐蚀相反，取的是局部最大值，效果是把图片”变胖”：
dilation = cv2.dilate(img, kernel)

cv2.imshow('erosion and dilation', np.hstack((img, erosion, dilation)))

# 开运算
# 先腐蚀后膨胀叫开运算（因为先腐蚀会分开物体，这样容易记住），其作用是：分离物体，消除小区域。这类形态学操作用cv2.morphologyEx()函数实现
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# 外面有噪点
img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/j_noise_out.bmp',0)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('opening', np.hstack((img, opening)))

# 闭运算
# 闭运算则相反：先膨胀后腐蚀（先膨胀会使白色的部分扩张，以至于消除/“闭合”物体里面的小黑洞，所以叫闭运算）
img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/j_noise_in.bmp', 0)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('closing', np.hstack((img, closing)))


cv2.waitKey(0)