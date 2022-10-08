import cv2
import numpy as np

pic = np.zeros((300,300,3),dtype="uint8")

cv2.line(pic,(0,0),(100,100),(255,0,255),3) #parametreleri görüntü, çizginin başladığı yer, bittiği yer,color, kalınlık
cv2.circle(pic,(150,150),25,(255,50,10),3) #2.parametre dairenin merkezi, yarıçap, color, kalınlık
cv2.putText(pic, "HISTAGE", (100,200), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1) #4.parametre yazı tipi, boyut, color, kalınlık

cv2.imshow("line circle text", pic)

cv2.waitKey(0)
cv2.destroyAllWindows()