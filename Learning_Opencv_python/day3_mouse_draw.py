'''
目标：
捕获鼠标事件
OpenCV函数：cv2.setMouseCallback()

知道鼠标在哪儿
OpenCV中，我们需要创建一个鼠标的回调函数来获取鼠标当前的位置、当前的事件如左键按下/左键释放或是右键单击等等，然后执行相应的功能。

使用cv2.setMouseCallback()来创建鼠标的回调函数，比如我们在左键单击的时候，打印出当前鼠标的位置：
'''

import cv2
import numpy as np 

# 鼠标的回调函数,参数是固定的
def mouse_event(event, x, y, flags, param):
    # 通过event判断具体是什么事件，这里是左键按下
    if event == cv2.EVENT_LBUTTONDOWN:
        print((x, y))


img = np.zeros((512, 512, 3), np.uint8) # 创建图片的时候类型就要np.uint8
cv2.namedWindow('image')

# 定义鼠标的回调函数
cv2.setMouseCallback('image', mouse_event)


while(True):
    cv2.imshow('image', img)
    # 按下ESC键退出
    if cv2.waitKey(20) == 27:
        break

'''
上面的代码先定义鼠标的回调函数mouse_event()，
然后在回调函数中判断是否是左键单击事件 EVENT_LBUTTONDOWN，是的话就打印出坐标。
需要注意的是，回调函数的参数格式是固定的，不要随意更改。
'''