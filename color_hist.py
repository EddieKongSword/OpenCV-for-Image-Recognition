import cv2
import numpy as np
import matplotlib.pyplot as plt

def flatten(mat):
    return np.ravel(mat)

img=cv2.imread('pxh01.jpg', 1)
# print(img.shape)
b=img[:, :, 0]
g=img[:, :, 1]
r=img[:, :, 2]
plt.subplot(311)
plt.hist(flatten(b), bins=30, facecolor='blue', edgecolor='white')
plt.subplot(312)
plt.hist(flatten(g), bins=30, facecolor='green', edgecolor='white')
plt.subplot(313)
plt.hist(flatten(r), bins=30, facecolor='red', edgecolor='white')
plt.show()
equ_b=cv2.equalizeHist(b)
equ_g=cv2.equalizeHist(g)
equ_r=cv2.equalizeHist(r)
equ=cv2.merge([equ_b, equ_g, equ_r])

cv2.imshow('img', img)
cv2.imshow('equ', equ)
cv2.waitKey(0)