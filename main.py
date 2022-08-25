import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    height=int(cap.get(4))
    width=int(cap.get(3))
    img =cv2.rectangle(frame,(100,100),(200,200),(128,120,120),5)
    img =cv2.circle(img,(300,300),60,(0,0,255),4)
    font=cv2.FONT_ITALIC
    img=cv2.putText(img, 'go go',(height,200),font,4,(0,0,0),5,cv2.LINE_AA)

    cv2.imshow('video1',img)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cap.destroyAllWindows()
