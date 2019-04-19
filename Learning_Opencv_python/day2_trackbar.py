'''
首先我们需要创建一个滑动条，如cv2.createTrackbar('R','image',0,255,call_back)，其中

参数1：滑动条的名称
参数2：所在窗口的名称
参数3：当前的值
参数4：最大值
参数5：回调函数名称，回调函数默认有一个表示当前值的参数

创建好之后，可以在回调函数中获取滑动条的值，
也可以用：cv2.getTrackbarPos()得到，其中，参数1是滑动条的名称，参数2是窗口的名称。
'''
import cv2
import numpy as np 

# 回调函数, x表示滑块的位置，本例子暂时不使用
def nothing(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# 创建RGB三个滑动条
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break

    # 获取滑块的值
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    # 设置img的颜色
    img[:] = [b, g, r]