import numpy as np
import cv2 as cv

img1=cv.imread('1.jpg')
logo=cv.imread('logo02.jpg')

#create a ROI(region of  interest)
rows, columns, channel=logo.shape
roi=img1[:rows, :columns]
logo_gary=cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
ret, mask=cv.threshold(logo_gary, 170, 255,cv.THRESH_BINARY)
mask_inv=cv.bitwise_not(mask)
x=cv.bitwise_and(roi, roi, mask=mask)
y=cv.bitwise_and(logo, logo, mask=mask_inv)
result=x+y

# cv.imshow("mask_inv", mask_inv)
# cv.imshow('mask', mask)
# cv.imshow('x', x)
# cv.imshow('y', y)
# cv.imshow('logo',logo)
# cv.imshow('result', result)
img1[:rows, :columns]=result
cv.imshow('mixed', img1)

cv.waitKey(0)
cv.destroyAllWindows()