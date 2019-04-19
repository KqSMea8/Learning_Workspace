import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg', 0)

# 灰度图显示，cmap(color, map)设置为gray
plt.imshow(img, cmap='gray')
plt.show()