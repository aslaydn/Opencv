import cv2
import numpy as np

#Basic canny edge detector

image = cv2.imread("efekt.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
# canny = cv2.Canny(blur,25,150)
# cv2.imshow("blurred image",blur)
# cv2.imshow("basic canny edge",canny)

#automatic canny edge detector

def autoCanny(blur,sigma=0.05):
    median = np.median(blur)
    lower=int(max(0,(1.0 - sigma)*median))
    upper=int(min(255,(1.0 + sigma)*median))
    canny = cv2.Canny(blur,lower,upper)
    return canny

wide = cv2.Canny(blur,20,250)
tight = cv2.Canny(blur,100,150)
auto = autoCanny(blur)

cv2.imshow("blurred image",blur)
#cv2.imshow("canny edges",np.hstack([wide,tight,auto]))
cv2.imshow("autocanny",auto)
cv2.waitKey(0)
cv2.destroyAllWindows()