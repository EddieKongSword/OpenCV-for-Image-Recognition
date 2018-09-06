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
labelArray=np.zeros(((posNum+negNum), 1), dtype=np.int32)

# positive examples
for i in range(posNum):
    filename='pos/'+str(i+1)+'.jpg'
    img=cv2.imread(filename)
    result=hog.compute(img=img, winStride=(8,8))
    for j in range(posNum):
        featureArray[i, j]=result[j]
    labelArray[i,0]=1  #正例

# negative examples
for i in range(negNum):
    filename = 'neg/' + str(i + 1) + '.jpg'
    img = cv2.imread(filename)
    result = hog.compute(img=img, winStride=(8, 8))
    for j in range(negNum):
        featureArray[posNum+i, j] = result[j]
    labelArray[posNum+i, 0] = -1   #负例

#define SVM
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

#train
result=svm.train(featureArray, cv2.ml.ROW_SAMPLE, labelArray)

#detect
alpha=np.zeros((1), dtype=np.float32)
rho=svm.getDecisionFunction(0, alpha)
detector=np.zeros((3781), dtype=np.float32)
detector[-1]=rho[0]
myHog=cv2.HOGDescriptor()
myHog.setSVMDetector(detector)
image= cv2.imread('Test2.jpg', 1)

#loacation information
info=myHog.detectMultiScale(image,0, (8, 8), (32, 32), 1.01, 2)
"""
winStride: (8, 8)
padding:  (32, 32)
"""
print(info, type(info))
x=int(info[0][0][0])
y=int(info[0][0][1])
w=int(info[0][0][2])
h=int(info[0][0][3])

#draw the rectangle
cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow('recognition', image)
cv2.waitKey(0)








