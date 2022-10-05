import cv2
import numpy as np

resim = cv2.imread("taehyung.jpg",0) #resmi okur. Resmi alıp numpy dizinine dönüştürür. ikinci parametre
#                                    olarak sıfır verirsek renkleri kullanmaz.

cv2.imshow("tae",resim) #resmi bu fonk. ile çağırırız. ilk parametre pencere açıldığında sol üstte 
#         yazdırmak istediğimiz şeyi yazarız. İkinci parametre göstermek istediğimiz resmi atarız.

cv2.imwrite("yeniresim.jpg",resim) #grileştirdiğim resmi yeniresim adında yeni bir jpg oluşturup kaydeder. 

print(resim) #her bir pikselin matrisler görünümünü verir.
print(resim.size) #görüntünün boyutunu verir.
print(resim.dtype) #hangi tipte veri kullandığını öğreniriz.
print(resim.shape) #genişliği, yüksekliği ve kaç kanaldan oluştuğunu gösterir. Değerlerin çarpımı size'ı verir.

cv2.waitKey(0) #kapanışta kullandığımız temel iskelet. Pencere açıldığında kapanması için bi tuşa basmamızı bekler.

cv2.destroyAllWindows() #çarpıya bastığımız zaman opencv'ye bağlı tüm pencereleri kapatırız.


