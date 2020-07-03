import cv2
import numpy as np
def sketch(image):
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gaussian=cv2.GaussianBlur(img_gray,(5,5),0)
    kernel_s=np.float32([-1,-1,-1,-1,8,-1,-1,-1,-1])
    #sharp=cv2.filter2D(img_gray,-1,kernel_s)
    canny=cv2.Canny(gaussian,10,60)
    kernel=np.ones((3,3),np.uint8)
    #opening=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
    ret,mask=cv2.threshold(canny,30,255,cv2.THRESH_BINARY_INV)
    return mask
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('sketck',sketch(frame))
    if(cv2.waitKey(1)==13):
        break
cap.release()
cv2.destroyAllWindows()