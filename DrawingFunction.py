
import numpy as np
import cv2

#create a black image 
img = np.zeros((512,512,3), np.uint8)
#arg1 = shape , arg2 = datatype

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),5)#增加長方形
img = cv2.circle(img,(447,63),63,(255,0,0),-1)#arg2:圓心座標，arg3:圓心半徑，-1代表填滿整個circle
ing = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#Draw a diagonal blue line with thickness of 5px
img = cv2.line(img,(0,0),(511,511),(0,0,255),5)##arg1:the input image ,arg2:initial position
#arg3:destination pos ,arg4:thickness of line
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('My img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()