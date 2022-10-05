import cv2
import numpy as np

resim = cv2.imread("joker.jpg")
uzatilanResim = cv2.copyMakeBorder(resim,120,120,100,400,cv2.BORDER_REPLICATE) 

cv2.imshow("Uzatilan joker",uzatilanResim)



cv2.waitKey(0)
cv2.destroyAllWindows()