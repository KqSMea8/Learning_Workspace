'''
现在我们来实现一个综合的例子，这个实例会帮助你理解图像交互的一些思想：

在图像上用鼠标画图，可以画圆或矩形，按m键在两种模式下切换。左键按下时开始画图，移动到哪儿画到哪儿，左键释放时结束画图。听上去很复杂，是吗？一步步来看：

用鼠标画图：需要定义鼠标的回调函数mouse_event
画圆或矩形：需要定义一个画图的模式mode
左键单击、移动、释放：需要捕获三个不同的事件
开始画图，结束画图：需要定义一个画图的标记位drawing
'''

import cv2
import numpy as np 

drawing = False # 是否开始画图
mode = True # True：画矩形，False：画圆
start = (-1, -1)

# 定义回调函数
def mouse_event(event, x, y, flags, param):
    # 在python中，变量不需要先声明，直接使用即可，那我们怎么知道用的是局部变量还是全局变量呢？
    #  首先：python使用的变量，在默认情况下一定是用局部变量。
    # 其次：python如果想使用作用域之外的全局变量，则需要加global前缀
    global start, drawing, mode

    # 左键按下： 开始画图
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 鼠标移动，画图
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
            else:
                cv2.circle(img, (x,y), 5,(0,0,255), -1)

    # 左键释放： 结束画图
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, start, (x, y), (0, 255, 0), 1)
        else:
            cv2.circle(img, (x, y), 5, (0,0,255), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event)

while(True):
    cv2.imshow('image', img)
    # 按下m切换模式
    if cv2.waitKey(1) == ord('m'):
        mode = not mode
    elif cv2.waitKey(1) == 27:
        break