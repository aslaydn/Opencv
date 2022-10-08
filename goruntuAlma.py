import cv2
import numpy as np

cam = cv2.VideoCapture(0) #parametre 0 dersek zaman bilgisayarın tanımlı kamerasını, 1 dersek usb'dekini, 2 ise videodaki görüntüleri alır. 

while True:
    ret, goruntu = cam.read() #görüntülerin döngü içinde döndürülmesiyle video oluşur.
    cv2.imshow("camera", goruntu)
    if cv2.waitKey(30)  & 0xFF == ord("q"):
        break

cam.release()

cv2.waitKey(0)
cv2.destroyAllWindows()    