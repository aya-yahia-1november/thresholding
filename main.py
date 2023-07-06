"""global thresholding"""
import cv2
import numpy as np

img = cv2.imread("boy.jpg", 0)
#_, th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
"""
اي قيمه pixel اقل من ال   55هتكون باللون الاسود في الاحداثيات
"""
_, th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img,125,255,cv2.THRESH_TRUNC)
"""
every value  less than 125
still orgen and remind pixels become 125
"""

_, th4 = cv2.threshold(img,55,255,cv2.THRESH_TOZERO)
"""
any value equal or less 55 become black
and other still orgen color
"""
_, th5 = cv2.threshold(img,55,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("image",img)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)

cv2.waitKey(0)
cv2.destroyAllWindows()





