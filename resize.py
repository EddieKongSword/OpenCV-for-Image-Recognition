import cv2 as cv

img=cv.imread('hxz02.jpg')
height, width=img.shape[:2]

changed01=cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
changed02=cv.resize(img, (int(height*0.8), int(width*0.7)), interpolation=cv.INTER_AREA)

print('original size', img.shape)
print('changed01 size', changed01.shape)
print('changed02 size', changed02.shape)

cv.imshow('original', img)
cv.imshow('01', changed01)
cv.imshow('02', changed02)
# cv.imwrite('hxz04.jpg', changed01)
cv.waitKey(0)
cv.destroyAllWindows()