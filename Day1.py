# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:29:24 2021

@author: User
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
# img = cv2.imread('D://ComputerVision//google.png',cv2.IMREAD_UNCHANGED)#Second argument is a flag which specifies the way image should be read.
# cv2.imshow('image',img)
# cv2.imwrite('Aaaaa.jpg',img)#在他的working directory 下放入Aaaaa.jpg 

# cv2.waitKey(0)
# cv2.destroyAllWindows()
##CV2 imread picture as BGR , so we need to cv2.COLOR_BGR2RGB
img = cv2.imread('D://ComputerVision//google.png',cv2.IMREAD_UNCHANGED)
img_rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

# plt.imshow(img)

# plt.axis('off')