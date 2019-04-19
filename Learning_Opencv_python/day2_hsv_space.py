'''
HSV是一个常用于颜色识别的模型，相比BGR更易区分颜色，转换模式用COLOR_BGR2HSV表示。

经验之谈：OpenCV中色调H范围为[0,179]，饱和度S是[0,255]，明度V是[0,255]。
虽然H的理论数值是0°~360°，但8位图像像素点的最大值是255，所以OpenCV中除以了2，
某些软件可能使用不同的尺度表示，所以同其他软件混用时，记得归一化。

现在，我们实现一个使用HSV来只显示视频中蓝色物体的例子，步骤如下：

捕获视频中的一帧
从BGR转换到HSV
提取蓝色范围的物体
只显示蓝色物体
'''
import numpy as np 
import cv2

capture = cv2.VideoCapture(0)

# 蓝色的范围，不同光照下不一样，可灵活调整
lower_blue = np.array([100,110, 110])
upper_blue = np.array([130, 255, 255])

while(True):
    # 1.捕获视频中的一帧
    ret, frame = capture.read()

    # 2.从BGR转换刀HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 3.inRange():介于lower/upper之间的为白色，其余为黑色
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 4.只保留原图中的蓝色部分
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break
