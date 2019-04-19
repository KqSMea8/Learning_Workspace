# 打开摄像头并灰度化显示
import cv2

capture = cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这一帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", gray)
    if cv2.waitKey(1) == ord('q'):
        break

'''
capture.read()函数返回的第1个参数ret(return value缩写)是一个布尔值，表示当前这一帧是否获取正确。
cv2.cvtColor()用来转换颜色，这里将彩色图转成灰度图。
另外，通过cap.get(propId)可以获取摄像头的一些属性，比如捕获的分辨率，亮度和对比度等。
propId是从0~18的数字，代表不同的属性,
eg.
# 获取捕获的分辨率
# propId可以直接写数字，也可以用OpenCV的符号表示
width, height = capture.get(3), capture.get(4)
print(width, height)
# 以原分辨率的一倍来捕获
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)

'''