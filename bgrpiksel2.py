import cv2
import numpy as np

joker = cv2.imread("joker.jpg")

joker[50,30]= [255,255,255] #pikseli beyaz ile değiştirdik

for i in range(100):
    joker[70,i] = [255,255,255]  #bir çizgi çekeriz.

cv2.imshow("joker",joker)


cv2.waitKey(0)
cv2.destroyAllWindows()