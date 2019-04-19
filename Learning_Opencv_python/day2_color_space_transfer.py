'''
目标：
颜色空间转换，如BGR↔Gray，BGR↔HSV等
追踪视频中特定颜色的物体
OpenCV函数：cv2.cvtColor(), cv2.inRange()
'''

# 颜色空间转换
import cv2

img = cv2.imread('lena.jpg')
# 转为灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
# cv2.waitKey(0)

'''
cv2.cvtColor()用来进行颜色模型转换，参数1是要转换的图片，参数2是转换模式， COLOR_BGR2GRAY表示BGR→Gray，可用下面的代码显示所有的转换模式：
'''
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)
'''
经验之谈：颜色转换其实是数学运算，如灰度化最常用的是：gray=R*0.299+G*0.587+B*0.114。
'''
