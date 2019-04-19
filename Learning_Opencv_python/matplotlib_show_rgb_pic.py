# 显示彩色图
# OpenCV中的图像是以 BGR 的通道顺序存储的，但Matplotlib是以 RGB 模式显示的，
# 所以直接在Matplotlib中显示OpenCV图像会出现问题，因此需要转换一下:

import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg')
img2 = img[:, :, ::-1]
'''
 img[:,:,0]表示蓝色通道，img[:,:,::-1]表示BGR翻转，变成RGB
 类似的，字符串s翻转可以这样写s[::-1],'abc'变成'cba',-1表示逆序
 图片是二位的，完整复制一张图像就是：
 img2 = img[:, :]
 而图片是有三个通道，相当于长度为3的字符串，所以通道翻转和复制组合起来就是img[:,:,::-1]
'''

# or use
# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 显示不正确的图
plt.subplot(121), plt.imshow(img)

# 显示正确的图
plt.subplot(122)
plt.xticks([]), plt.yticks([]) # 隐藏x和y轴
plt.imshow(img2)

plt.show()