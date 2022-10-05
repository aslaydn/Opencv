import cv2
import numpy as np

resim = cv2.imread("jinx.jpg")
aynalananResim = cv2.copyMakeBorder(resim,400,300,300,400,cv2.BORDER_REFLECT) 
#parametreleri: aynalanacak resim, boyutlar(üst,alt,sol,sağ), sınırları tekrarla

cv2.imshow("Aynalanan jinx",aynalananResim)



cv2.waitKey(0)
cv2.destroyAllWindows()