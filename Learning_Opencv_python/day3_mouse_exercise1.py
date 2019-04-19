'''
实现用鼠标画矩形，跟实例差不多，但只实时画一个
'''

import numpy as np 
import cv2 
# 不能这样写，这样写start和end共享内存了
# start = end = (0,0)
start, end = (0, 0), (0, 0)
drawing = False

# 定义回调函数
def mouse_event(event, x, y, flags, param):
    global start, end, drawing,tmp # 为什么tmp也要使用全局呢，因为tmp是copy来的，要在tmp上获取x，y并且画图
    
    # 鼠标按下，开始画图：记录下起点
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 实时移动的位置作为矩形的终点
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end = (x, y)
    # 鼠标停止后，停止绘图
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False 
        cv2.rectangle(img, start, (x, y), (255, 0, 0), 2) # 这句话是不是会把img的图片显示到window上
        # 要加下面这句
        start = end = (0,0)

img = np.zeros((512, 512, 3), np.uint8)
# 要给窗口命名
cv2.namedWindow('image')
#不要忘了设置鼠标的回调函数, 鼠标的回调函数是绑定了名为'image'的窗口上的
cv2.setMouseCallback('image', mouse_event)

while(True):
    # 拷贝出原图，这样才能实时画一个矩形
    tmp = np.copy(img)
    if(drawing and end != (0, 0)):
        cv2.rectangle(tmp, start, end, (255, 0, 0), 2)

    cv2.imshow('image', tmp)
    if cv2.waitKey(1) == ord('q'):
        break
