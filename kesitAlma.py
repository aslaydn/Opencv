import cv2
import numpy as np

jinx = cv2.imread("jinx.jpg")
kesit = jinx[150:350,400:500] #y,x
jinx[0:200,0:100] = kesit #kestiğim bölgeyi resim üzerinde yapıştırmak için, aynı boyutta olmalı.
jinx[400:450,300:350] = (150,0,255)
cv2.imshow("kesit alanı", kesit)
cv2.imshow("jinx",jinx)

cv2.waitKey(0)
cv2.destroyAllWindows()