import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit=np.array([38,100,100])
    upperLimit=np.array([75,255,255])
    mask=cv2.inRange(hsv,lowerLimit,upperLimit)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
