import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, view = cam.read()
    cv2.rectangle(view,(100,100),(200,200),(0,0,255),3)
    cv2.line(view,(0,0),(100,100),(34,78,156),2)
    cv2.circle(view,(150,150),50,(80,150,35),2)
    cv2.putText(view,"HISTAGE",(220,220),cv2.FONT_HERSHEY_DUPLEX,1,(200,0,0),2)
    cv2.imshow("HISTAGE", view)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cam.release()   

cv2.destroyAllWindows()