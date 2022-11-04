from xml.dom import HierarchyRequestErr
import cv2
img = cv2.imread("kontur.png")

#gri tonlu görüntülerin işlenmesi daha kolay olduğu için önce griye çeviririz.
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edged= cv2.Canny(gray,50,200)
cv2.imshow("edged",edged)

contours,Hierarchy=cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #kontür modu ve kontür yaklaşım metodu
print("Numbers of Contours: ",len(contours))
cv2.drawContours(img,contours,-1,(255,0,0),4)
cv2.imshow("contours",img)

cv2.waitKey(0)
cv2.destroyAllWindows()