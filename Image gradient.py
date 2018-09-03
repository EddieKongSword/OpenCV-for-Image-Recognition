import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img=cv.imread('stone01.jpg')
laplacian=cv.Laplacian(img, cv.CV_64F)
# laplacian_abs=cv.convertScaleAbs(laplacian)
laplacian_abs=np.uint8(np.abs(laplacian))
sobelX=cv.Sobel(img, cv.CV_64F,1,0)
sobelX_abs=cv.convertScaleAbs(sobelX)
sobelY=cv.Sobel(img, cv.CV_64F,0,1)
sobelY_abs=cv.convertScaleAbs(sobelY)
print(laplacian_abs[1,1])
print(laplacian[1,1])

added_sobel=cv.addWeighted(sobelX_abs,0.5, sobelY_abs, 0.5, 0)
plt.subplot(131)
plt.imshow(img)
plt.title('original')
plt.subplot(132)
plt.imshow(added_sobel)
plt.title('added sobel')
plt.subplot(133)
plt.imshow(laplacian_abs)
plt.title('laplacian int8')
plt.show()

# cv.imshow('added sobel', added_sobel)
# cv.imshow('original', img)
# cv.imshow('laplacian int8', laplacian_abs)


cv.waitKey(0)
cv.destroyAllWindows()








