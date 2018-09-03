import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('1.jpg')
print('img shape', img.shape)

# img2 = img[::-1,::-1] #可以使图像上下颠倒,或者旋转180度

#提取R G B
# b,g,r=cv.split(img)
b, g, r=img[:, :, 0], img[:, :, 1], img[:, :, 2]
img2=cv.merge([r,g,b])

plt.subplot(121)
plt.title('BGR')
plt.imshow(img)
plt.axis('off')
plt.subplot(122)
plt.title('RGB')
plt.imshow(img2)
# xtick 和 ytick 输入为空列表，以此隐藏tick
plt.xticks([])
plt.yticks([])
plt.show()
