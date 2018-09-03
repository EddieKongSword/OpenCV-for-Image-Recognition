import cv2 as cv

img=cv.imread('stone01.jpg', 0)
edges01=cv.Canny(img, 100, 200)
edges02=cv.Canny(img, 150, 220)


cv.imshow('img', img)
cv.imshow('edges01', edges01)
cv.imshow('edges02', edges02)
cv.waitKey(0)
cv.destroyAllWindows()
