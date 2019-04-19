'''
访问和修改图片像素点的值
获取图片的宽、高、通道数等属性
了解感兴趣区域ROI
分离和合并图像通道
'''
# 获取和修改像素点值
import cv2
img = cv2.imread('lena.jpg')
'''
通过行列的坐标来获取某像素点的值，对于彩色图，结果是B,G,R三个值的列表，对于灰度图或单通道图，只有一个值：
'''
px = img[100, 90]
print(px) # [83 94 198]

# 只获取蓝色blue通道的值
px_blue = img[100, 90, 0]
print(px_blue)
'''
行对应y，列对应x，所以其实是img[y, x]，需要注意噢(●ˇ∀ˇ●)。容易混淆的话，可以只记行和列，行在前，列在后
注意：这步操作只是内存中的img像素点值变了，因为没有保存，所以原图并没有更改。
'''
img[100, 90] = [255, 255, 255]
print(img[100, 90])
'''
经验之谈：还有一种性能更好的方式，获取：img.item(100,100,0)，修改：img.itemset((100,100,0),255)，但这种方式只能B,G,R逐一进行。
'''

# 图片属性
'''
img.shape获取图像的形状，图片是彩色的话，返回一个包含行数（高度）、列数（宽度）和通道数的元组，灰度图只返回行数和列数
'''
print(img.shape)
# shape中包括行数，列数和通道数
height, width, channels = img.shape

# img.dtype获取图像数据类型
print(img.dtype) # uint8
# 经验之谈：很多错误都是因为数据类型不对导致的，所以健壮的代码应该对这个属性加以判断。


# img.size获取图像总像素数
print(img.size) # 350*350*3=367500


# ROI
'''
ROI：Region of Interest，感兴趣区域。什么意思呢？
比如我们要检测眼睛，因为眼睛肯定在脸上，所以我们感兴趣的只有脸这部分，其他都不care，
所以可以单独把脸截取出来，这样就可以大大节省计算量，提高运行速度。
'''
# 截取脸部ROI
face = img[120:270,145:230]
# cv2.imshow('face', face)
# cv2.waitKey(0)

# 通道分割与合并
'''
彩色图的BGR三个通道是可以分开单独访问的，也可以将单独的三个通道合并成一副图像。
分别使用cv2.split()和cv2.merge()：
'''
b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

# split()函数比较耗时，更高效的是用numpy中的索引
b = img[:,:, 0]
cv2.imshow('bule',b)
cv2.waitKey(0)