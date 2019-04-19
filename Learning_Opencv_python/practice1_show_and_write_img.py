import cv2
# 要用绝对路径
img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg')
cv2.imshow('lena.jpg', img)
k = cv2.waitKey(0)
# ord(c)返回 字符串对应的十进制整数
if k == ord('s'):
    cv2.imwrite('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena_save.bmp', img)