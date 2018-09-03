import  numpy as np
import cv2 as cv

img1=cv.imread('1.jpg')
img2=cv.imread('6.jpg')
print(img1.shape)
print(img2.shape)
box1=img1[:350,:350]
box2=img2[:350,:350]

img3=cv.addWeighted(box1,0.7, box2, 0.3, 0)

cv.imshow('added', img3)
cv.waitKey(0)
cv.destroyAllWindows()
