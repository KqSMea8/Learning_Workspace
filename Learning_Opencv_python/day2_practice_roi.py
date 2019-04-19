# 打开lena.jpg，将帽子部分（高：25~120，宽：50~220）的红色通道截取出来并显示

import cv2

img = cv2.imread('lena.jpg')

hat = img[25:120, 50:220,2]

cv2.imshow('hat', hat)
cv2.waitKey(0)