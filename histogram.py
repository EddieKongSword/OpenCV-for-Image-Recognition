import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Unequalized_Hawkes_Bay_NZ.jpg', 0)
# print(img.shape)
cv2.imshow('img', img)
img_flatten=np.ravel(img)
equ = cv2.equalizeHist(img)
cv2.imshow('equ',equ)
equ_flatten=np.ravel(equ)
plt.subplot(211)
plt.hist(equ_flatten, bins=30, facecolor='red', edgecolor='black')
#bins, 条个数
plt.subplot(212)
plt.hist(img_flatten, bins=30, facecolor='green', edgecolor='black')
cv2.imshow('equ',equ)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()