import cv2
import numpy as np

def nothing(x): #trackbar kullanırken bazı funcları kullanmamak için.
    pass

cap=cv2.VideoCapture(0)
""" cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H","Trackbars",0,180,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
cv2.createTrackbar("U-H","Trackbars",180,180,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing) """

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #kırmızı objeleri algılamak için
    
    #l_h=cv2.getTrackbarPos("L-H","Trackbars")
    #l_s=cv2.getTrackbarPos("L-S","Trackbars")
    #l_v=cv2.getTrackbarPos("L-V","Trackbars")
    #u_h=cv2.getTrackbarPos("U-H","Trackbars")
    #u_s=cv2.getTrackbarPos("U-S","Trackbars")
    #u_v=cv2.getTrackbarPos("U-V","Trackbars") 

    lower_red=np.array([0,70,50])
    upper_red=np.array([10,255,255])

    mask=cv2.inRange(hsv,lower_red,upper_red) #sadece kırmızı obje beyaz, diğerleri siyah olmalı.
    kernel=np.ones((5,5),np.uint8) #black square oluşturduk
    mask=cv2.erode(mask,kernel)

    #contours detection
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        x=approx.ravel() [0]
        y=approx.ravel() [1]
        
        if area>400:
            cv2.drawContours(frame,[approx],0,(0,0,0),5)

            if len(approx)==4:
                cv2.putText(frame,"rectangle",(x,y),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0))

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
