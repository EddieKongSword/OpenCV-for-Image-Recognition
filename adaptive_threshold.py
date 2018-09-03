import cv2 as cv

def nothing(x):
    pass
img=cv.imread('pxh02.jpg',0)
cv.namedWindow('image')
cv.createTrackbar('block size', 'image', 5, 12, nothing)
cv.createTrackbar('C value', 'image', 1, 5, nothing)
while True:
    k = cv.waitKey(100)
    if k==27:
        break
    block_size=cv.getTrackbarPos('block size', 'image')
    c_value=cv.getTrackbarPos('C value', 'image')
    img_threshold=cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY, block_size, c_value)
    cv.imshow('image', img_threshold)




cv.destroyAllWindows()
