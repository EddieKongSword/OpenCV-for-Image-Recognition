import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pxh01.jpg', )
move=np.array([
    [1,0,50],
    [0,1,100]
], dtype=np.float32)
row, column=img.shape[:2]

img_=cv2.warpAffine(img, move,dsize=[row, column])

