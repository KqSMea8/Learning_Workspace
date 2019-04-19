'''
目标：
图片间的数学运算，如相加、按位运算等
OpenCV函数：cv2.add(), cv2.addWeighted(), cv2.bitwise_and()
'''

# 图片相加
# 要叠加两张图片，可以用cv2.add()函数，相加两幅图片的形状（高度/宽度/通道数）必须相同。
# numpy中可以直接用res = img + img1相加，但这两者的结果并不相同
import numpy as np 
import cv2
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))  # 250 + 10 = 260 => 255
print(x + y) # 260 % 256 = 4

# 如果是二值化图片（只有0和255两种值），两者结果是一样的（用numpy的方式更简便一些）

# 图像混合 cv2.addWeighted()  也是一种图片相加的操作，只不过两幅图片的权重不一样，γ相当于一个修正值：

img1 = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena_small.jpg')
img2 = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/opencv-logo-white.png')
res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# 当alpha和beta都等于1的时候，就相当于图片加成


# 按位操作
# 思路就是把原图中要放logo的区域抠出来，再把logo放进去就行了：
img3 = cv2.imread("/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg")

# 把logo放在左上角
rows, cols = img2.shape[:2]
# 浅拷贝, roi改变 img3[:rows, :cols]也会改变
roi = img3[:rows, :cols]

# 创建掩膜
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) # 此时圈圈是白色的，也就是255，别的地方都是0
mask_inv = cv2.bitwise_not(mask)

# 保留除了logo外的背景,然后将相与之后的图片给img3_bg，现在它是一张带有lena并且中间是黑色的
img3_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# 将opencv图标和img3_bg相加，opencv图标很显然只有rgb颜色，其他地方都是透明的（我理解就是没有值，默认为0吧）
dst = cv2.add(img3_bg, img2) # 进行融合
# 因为python变量的原因，roi之间不能共享内存，所以最后还得将dst赋值回给img3
img3[:rows, :cols] = dst 
# if img3[:rows, :cols].all() == roi.all():
#     print("good")


cv2.imshow('addWeighted', img3)
cv2.waitKey(0)