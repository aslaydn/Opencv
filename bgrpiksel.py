import cv2
import numpy as np

jjk = cv2.imread("jk.jpg")
jjk = cv2.resize(jjk,(640,480))
cv2.imshow("Jungkook Jeon", jjk)

print(jjk[(230,80)]) #aşağı doğru 230, sağa doğru 80 piksel gidildiğinde o piksel neyse(BGR değeri) onu belirttik.
print(f"Resmin boyutu: {jjk.size}")
print(f"Resmin özellikleri: {jjk.shape}")
print(f"Resmin veri tipi: {jjk.dtype}")


cv2.waitKey(0)
cv2.destroyAllWindows()
