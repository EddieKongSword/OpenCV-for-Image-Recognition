import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pxh01.jpg', 1)
cow, column=img[:2]
for m in range(100, 300):
    for n in range(300, 600):
        if m%10==0 and n%10==0:
            for i in range(10):
                for j in range(10):
                    (b, g, r)=img[m,n]
                    img[m-i, n-j]=(b, g, r)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()