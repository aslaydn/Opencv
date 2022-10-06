import cv2
import numpy as np

resim = cv2.imread("renault.jpg") #ikinci parametreye 0 yazdığımız zaman da resmi grileştirir.
griResim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

yukseklik,genislik,kanalSayisi = resim.shape
print("Orijinal", yukseklik, genislik, kanalSayisi)
yukseklik2,genislik2 = griResim.shape
print("Gri Resim",yukseklik2,genislik2)

cv2.imshow("orijinal resim", resim)
cv2.imshow("gri resim", griResim)

cv2.waitKey(0)
cv2.destroyAllWindows()