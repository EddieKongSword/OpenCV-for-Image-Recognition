import cv2 as cv
import numpy as np

img=cv.imread('stone01.jpg')
length, width=img.shape[:2]
wall=np.zeros([length, width,1], dtype=np.uint8)
gary=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, threshold=cv.threshold(gary, 127, 255, 0)

#函数cv2.findContours() 有三个参数，第一个是输入图像，
# 第二个是轮廓检索模式，第三个是轮廓近似方法。
image01, contours01, construction01=cv.findContours(threshold, 2,
                                                    cv.CHAIN_APPROX_NONE)
# img = cv.drawContours(img, contours01, 3, (0,255,0), 3)
# cnt=contours01[0]
# M=cv.moments(cnt)
# area = cv.contourArea(cnt)
# print(cnt)
# print(area)
print(contours01)

for i in range(int(length)):
    for j in range(int(width)):
        if [[i,j]] in contours01[-1]:
            wall[i ,j]=255
cv.imshow('trace', wall)



# cv.imshow('threshold', threshold)
# cv.imshow('img', img)
# cx=int(M['m10']/M['m00'])
cv.waitKey(0)
cv.destroyAllWindows()