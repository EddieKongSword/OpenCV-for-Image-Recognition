import cv2 as cv

img=cv.imread('hxz02.jpg')
row,column=img.shape[:2]

M=cv.getRotationMatrix2D(( int(row/2),int(column/2)), 90, 1)
result=cv.warpAffine(img, M, (int(row*1.5), int(column*1.5)))

cv.imshow('rotation result', result)
cv.waitKey(0)
cv.destroyAllWindows()