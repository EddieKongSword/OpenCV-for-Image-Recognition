import cv2
import numpy as np
import matplotlib.pyplot as plt

#9*4*105=3780
posNum=820
negNum=1931
winSize=(64,128)
blockSize=(16,16)
blockStride=(8,8)
cellSize=(8,8)
binNum=9
featureNum=3780

#create Hog and SVM
hog=cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, binNum)
svm=cv2.ml.SVM_create()

featureArray=np.zeros(((posNum+negNum), featureNum), dtype=np.float32)
labelArray=np.zeros(((posNum+negNum), 1), dtype=np.int8)

# positive examples
for i in range(posNum):
    filename='pos/'+str(i+1)+'.jpg'
    img=cv2.imread(filename)
    result=hog.compute(img=img, winStride=(8,8))
    for j in range(posNum):
        featureArray[i, j]=result[j]
    labelArray[i,0]=1

# negative examples
for i in range(negNum):
    filename = 'neg/' + str(i + 1) + '.jpg'
    img = cv2.imread(filename)
    result = hog.compute(img=img, winStride=(8, 8))
    for j in range(negNum):
        featureArray[posNum+i, j] = result[j]
    labelArray[posNum+i, 0] = -1

#define SVM
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

#train