import cv2

img=cv2.imread('pxh01.jpg',0)
cv2.imshow('img', img)
equ=cv2.equalizeHist(img)
cv2.imshow('equ', equ)
cv2.waitKey(0)
cv2.destroyAllWindows()