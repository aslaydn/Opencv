from pickletools import uint8
import cv2
import numpy as np

pic = np.zeros((300,300,3), dtype="uint8") #parametreler shape, dtype. bu fonksiyon tüm elemanları 0 olan matris oluşturur.
print(pic)

cv2.waitKey(0)
cv2.destroyAllWindows()