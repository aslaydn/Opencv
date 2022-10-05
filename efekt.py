import cv2
import numpy as np

joker = cv2.imread("joker.jpg")

# joker[:,:,0] = 255 #bgr kısmınıa 0 dediğimizde blue kısmı devreye girer. 1 verirsek green efekt olur. 2 verirsek red olur.
# joker[:,:,2] = 255 #blue red karışımı efekt uygular. (255 yazmak zorunda değiliz.)
joker[160:270,600:1280,0] =255 #belli bir kısma efekt uygulamak istersek: ilk parametre y, ikinci parametre x.
joker[160:270,600:1280,2] =255                  

cv2.imshow("Joker", joker)
cv2.imwrite("efekt.jpg",joker)

cv2.waitKey(0)
cv2.destroyAllWindows()