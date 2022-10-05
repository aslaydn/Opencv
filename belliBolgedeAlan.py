import cv2
import numpy as np

resim= cv2.imread("hababam.jpg")
cv2.rectangle(resim,(250,230),(330,110),[0,0,255],3) #sol alt köşe, sağ üst köşe. bu kez x,y şeklnide. 4.parametre BGR,
#                                                 5. parametre çerçeve kalınlığı, 0-9 arasında.
cv2.imshow("hababam",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()