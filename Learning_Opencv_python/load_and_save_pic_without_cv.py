# 不使用opencv，matplotlib也可以加载和保存图片

import matplotlib.image as pli
import matplotlib.pyplot as plt

img = pli.imread('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena.jpg')
plt.imshow(img)

# 保存图片，需要放在show()之前
plt.savefig('/home/sanjay/Workspace/learning/Learning_Opencv_python/lena2.jpg')
plt.show()