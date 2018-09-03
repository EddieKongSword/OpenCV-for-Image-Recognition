import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img0=cv.imread('hxz02.jpg')
img=cv.cvtColor(img0, cv.COLOR_BGR2RGB)
row, column=img.shape[:2]

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv.getPerspectiveTransform(pts1,pts2)
dst=cv.warpPerspective(img,M,(column, row))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()