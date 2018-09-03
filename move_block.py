import cv2 as cv
import numpy as np

img=cv.imread('1.jpg')
cv.imshow('img', img)
img0=img

# print(img.shape)

box=img[280:340, 330:390]
img[100:160, 110:170]=box
cv.imshow('ing_box', img)

img0[:, :, 2]=0
cv.imshow('img0', img0)


cv.waitKey(0)
cv.destroyAllWindows()

