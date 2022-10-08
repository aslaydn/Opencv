import cv2
import numpy as np

pic = cv2.imread("filter.png")
meanFilter = cv2.blur(pic,(3,3))
meanFilter2 = cv2.blur(pic,(5,5))

gauss = cv2.GaussianBlur(pic,(3,3),0)
gauss2 = cv2.GaussianBlur(pic, (5,5),0)

medianFilter = cv2.medianBlur(pic,3)
medianFilter2 = cv2.medianBlur(pic,5)

cv2.imshow("original pic",pic)
cv2.imshow("mean 3x3", meanFilter)
cv2.imshow("mean 5x5",meanFilter2)

cv2.imshow("median 3x3",meanFilter)
cv2.imshow("median 5x5", meanFilter2)

cv2.imshow("gauss 3x3",gauss)
cv2.imshow("gauss 5x5", gauss2)

cv2.waitKey(0)
cv2.destroyAllWindows()