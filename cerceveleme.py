import cv2
import numpy as np

resim = cv2.imread("anime.png")
resim = cv2.resize(resim,(480,360))
tekrarlananResim = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT, value = (50,0,255)) 

cv2.imshow("Cercevelenen anime girl",tekrarlananResim)



cv2.waitKey(0)
cv2.destroyAllWindows()