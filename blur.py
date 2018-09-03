import cv2 as cv

def nothing(x):
    pass

img=cv.imread('pxh02.jpg')
cv.namedWindow('image')
cv.createTrackbar('GaussianBlur_kSize','image', 1, 10, nothing)
cv.createTrackbar('sigmaX', 'image', 1, 10, nothing)

while(1):
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    size = cv.getTrackbarPos('GaussianBlur_kSize', 'image')
    sigma=cv.getTrackbarPos('sigmaX', 'image')
    img_blur = cv.GaussianBlur(img, (size, size), sigmaX=sigma)
    cv.imshow('image', img_blur)

cv.destroyAllWindows()


