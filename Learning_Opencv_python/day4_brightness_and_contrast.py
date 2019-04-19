'''
亮度调整是将图像像素的强度整体变大/变小，对比度调整指的是图像暗处的像素强度变低，亮出的变高，从而拓宽某个区域内的显示精度。

OpenCV中亮度和对比度应用这个公式来计算：g(x)=αf(x)+β，其中：α(>0)、β常称为增益与偏置值，分别控制图片的对比度和亮度
'''
import cv2
import numpy as np 
import ipdb 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg')

#还记得图像混合那一节中numpy对数据溢出的取模处理吗？250+10 = 260 => 260%256=4，
# 它并不适用于我们的图像处理，所以用np.clip()函数将数据限定：a<0 => a=0, a>255 => a=255。
res = np.uint8(np.clip((1.5 * img + 20), 0, 255))

#ipdb.set_trace() 
# 两张图片横向合并，便于比较
tmp = np.hstack((img, res))

cv2.imshow('image', tmp)
cv2.waitKey(0)