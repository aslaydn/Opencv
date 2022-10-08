import cv2
import numpy as np

pic = cv2.imread("anime.png")
ikiKatBuyuk = cv2.pyrUp(pic)
ikiKatKucuk = cv2.pyrDown(pic)

print("orijinal resim",pic.shape)
print("iki kat buyuk resim", ikiKatBuyuk.shape)
print("iki kat kucuk resim", ikiKatKucuk.shape)

cv2.imshow("orijinal", pic)
cv2.imshow("iki kat", ikiKatBuyuk)
cv2.imshow("iki kat kucuk resim", ikiKatKucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()