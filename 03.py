import cv2 as cv
import numpy as np



img = cv.imread('6.jpg')
cv.imshow('img',img)
# print(img[0][0])

gary=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gary', gary)


# # 提取 BGR
b,g,r=cv.split(img)

# # RGB output
# img2=cv.merge([r,g,b])
# cv.imshow('img2', img2)


zero=np.zeros(img.shape,dtype=np.uint8)

blue=zero
blue[:, :, 0]=b
cv.imshow('blue', blue)
#
# green=zero
# green[:, :, 1]=g
# cv.imshow('green', green)
#
# red=zero
# red[:, :, 2]=r
# cv.imshow('red', red)

# blue_green_red=zero
# blue_green_red[:, :, 0]=b
# blue_green_red[:, :, 1]=g
# blue_green_red[:, :, 2]=r
# cv.imshow('blue&green', blue_green_red)
# print(blue_green_red[0][0])



cv.waitKey()
cv.destroyAllWindows()





