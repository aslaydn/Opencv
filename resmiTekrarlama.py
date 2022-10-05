import cv2
import numpy as np

resim = cv2.imread("anime.png")
resim = cv2.resize(resim,(480,360))
tekrarlananResim = cv2.copyMakeBorder(resim,200,400,400,500,cv2.BORDER_WRAP) 

cv2.imshow("Tekrarlanan anime girl",tekrarlananResim)



cv2.waitKey(0)
cv2.destroyAllWindows()