
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:27:58 2017

@author: Öğrenci
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('mertcan.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    r = 100.0 / gray.shape[1]
    dim = (100, int(gray.shape[0] * r))
 
# perform the actual resizing of the image and show it
    resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("resized", resized)

    
    
    
    
    
    #cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
