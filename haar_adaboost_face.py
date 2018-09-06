import cv2

#load xml and image
face_xml=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml=cv2.CascadeClassifier('haarcascade_eye.xml')
img=cv2.imread('face_06.jpg')
# cv2.imshow('img', img)
gary=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#choose color
face_color=(20,150,0)
eyes_color=(106 ,106, 255)

#detect face and eyes
faces=face_xml.detectMultiScale(gary, scaleFactor=1.3, minNeighbors=5)
print('face=', len(faces))
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), face_color, 2)
    roi_face=gary[y:y+h, x:x+w]
    roi_color=img[y:y+h, x:x+w]
    eyes=eye_xml.detectMultiScale(image=roi_face, scaleFactor=1.3, minNeighbors=3)
    # eyes=eye_xml.detectMultiScale(roi_face)
    print('eyes=', len(eyes))
    for (e_x, e_y, e_w, e_h) in eyes:
        cv2.rectangle(roi_color, (e_x, e_y), (e_x+e_w, e_y+e_h), eyes_color, 2)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()