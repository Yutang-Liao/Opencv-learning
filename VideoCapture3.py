import numpy as np 
import cv2

cap = cv2.VideoCapture(0) ##創造一個物件cap 去捕捉

#Define codec and create Videowriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi',fourcc,20.0, (640,480),0 ) ##創造一個out物件去儲存,arg1 = output
##名稱 ,arg2 = 編碼名稱,arg3 = fps ,arg4 = windows size ,arg 5 請參考網址
## https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html

while(cap.isOpened()):
    ret , frame = cap.read()##capture frame by frame 
    if ret == True:
        ##翻轉畫面
        #frame = cv2.flip(frame,0)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #write the flipped name
        #out.write(frame)
        out.write(gray)

        cv2.imshow('frame',frame)
        cv2.imshow('gray_frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
        
    