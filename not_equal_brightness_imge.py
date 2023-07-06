import cv2
import numpy as np
img= cv2.imread("text.jpg",0)
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,4);
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,4);
cv2.imshow("image",th1)
cv2.imshow("THRESH_MEAN_C",th2)
cv2.imshow("THRESH_GAUSSIAN_C",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
بيوضح الصور الي الاضاء بتعتها غير بعض 
ازاي عن طريق فصل الخلفيه وزياده توضيح الكلام
"""