import numpy as np 
import cv2
cap = cv2.VideoCapture('C:\\Users\\User\\vtest.avi')

while(True):
    #capture frame by frame 
    ret ,frame = cap.read()
    
    #Our operations on the frame come here
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #display 
    cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):##25ms delay 
        break

#release the capture
cap.release()
cv2.distroyAllwindows()