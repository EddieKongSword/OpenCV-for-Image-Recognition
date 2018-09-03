import cv2
import numpy as np
#create data
g=np.array([[155,45],[157,47],[160,51],[162,55],[165,57]])
b=np.array([[167,60],[170,62],[172,64],[179,67],[181,67]])
label=np.array([[0],[0],[0],[0],[0],[1],[1],[1],[1],[1]])
data1=np.vstack((g,b))
data1=np.array(data1, dtype=np.float32)

#create SVM
svm=cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(1.0)

#train
result=svm.train(data1, cv2.ml.ROW_SAMPLE, label)

#prediction
p_data=np.array([[167,55],[170,65]],dtype=np.float32)
print(p_data.shape,type(p_data))
(res, p_label)=svm.predict(p_data)
print(p_label)

