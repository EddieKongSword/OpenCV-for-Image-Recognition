import numpy as np
import cv2 as cv
# Load an color image
img = cv.imread('1.jpg', 1)
cv.imshow('img1', img)
key=cv.waitKey(0)
if key==27:
    cv.destroyAllWindows()
if key==ord('s'):
    cv.imwrite('Zach LaVine.png', img)
    cv.destroyAllWindows()






