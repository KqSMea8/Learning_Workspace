'''
看得出来固定阈值是在整幅图片上应用一个阈值进行分割，它并不适用于明暗分布不均的图片。 
cv2.adaptiveThreshold()自适应阈值会每次取图片的一小部分计算阈值，这样图片不同区域的阈值就不尽相同。它有5个参数，其实很好理解，先看下效果：
'''
# 自适应阈值对比固定阈值
import cv2
import matplotlib.pyplot as plt 
img = cv2.imread('sudoku.jpg', 0)

# 固定阈值
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 自适应阈值
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4
)

th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6
)

titles = ['Original', 'Global(v = 127)', 'Adaptive mean', 'Adaptive gaussian']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()

'''
参数1：要处理的原图
参数2：最大阈值，一般为255
参数3：小区域阈值的计算方式
ADAPTIVE_THRESH_MEAN_C：小区域内取均值
ADAPTIVE_THRESH_GAUSSIAN_C：小区域内加权求和，权重是个高斯核
参数4：阈值方式（跟前面讲的那5种相同）
参数5：小区域的面积，如11就是11*11的小块
参数6：最终阈值等于小区域计算出的阈值再减去此值

在前面固定阈值中，我们是随便选了一个阈值如127，那如何知道我们选的这个阈值效果好不好呢？
答案是：不断尝试，所以这种方法在很多文献中都被称为经验阈值。
Otsu阈值法就提供了一种自动高效的二值化方法，不过我们直方图还没学，这里暂时略过
'''