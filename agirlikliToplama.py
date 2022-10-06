import cv2
import numpy as np

resim1 = cv2.imread("anime.png")
resim1 = cv2.resize(resim1,(640,480))

resim2 = cv2.imread("kakegurui.jpg")
resim2 = cv2.resize(resim2,(640,480))

print(resim1[100,230]) #pikseldeki BGR değerlerini yazdırır.
print(resim2[300,430])

print(resim1[100,230] + resim2[300,430]) #BGR değerlerini toplar.

toplam = cv2.add(resim1,resim2) #resmi üst üste toplar, aynı boyutta olması lazım.
agirlikliToplama = cv2.addWeighted(resim1,0.7,resim2,0.3,0) #hangi resmi hangi oranda kullanacağımızı parametre
#                                       olarak giriyoruz.(oranların toplamı 1 olmalı.) son parametre her zaman 0.

cv2.imshow("toplanmis resim",toplam)
cv2.imshow("agirlikli toplama", agirlikliToplama)
cv2.imwrite("addingpics.jpg",toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()