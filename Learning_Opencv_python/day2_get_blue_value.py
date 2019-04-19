'''
蓝色的HSV值的上下限lower和upper范围是怎么得到的呢？其实很简单，我们先把标准蓝色的BGR值用cvtColor()转换下：
'''
import numpy as np 
import cv2

blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)