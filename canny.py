import cv2
import matplotlib.pyplot as plt

img0=cv2.imread('pxh01.jpg', 1)
img=cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(img, 150, 200, )
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()

