import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('hxz02.jpg')
row, column=img.shape[:2]
img_RBG=cv.cvtColor(img, cv.COLOR_BGR2RGB)

point1=np.float32([[50,50], [200, 50], [50, 200]])
point2=np.float32([[10,100], [200,50],[100,250]])

M=cv.getAffineTransform(point1, point2)

dst=cv.warpAffine(img_RBG, M, (column*2, row*2))

# cv.imshow('affine', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()
plt.subplot(121)
plt.title('input')
plt.imshow(img_RBG)
plt.subplot(122)
plt.title('output')
plt.imshow(dst)
plt.show()