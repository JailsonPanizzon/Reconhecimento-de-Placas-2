import cv2
import numpy as np

class cl:
    def detect(img,cor):
        kernel = np.ones((5 , 5), np.uint8)
        cord = []
        val = 5
        rangomax = np.array([int(cor[0])+val,int(cor[1])+val,int(cor[2])+val])
        rangomin = np.array([int(cor[2])-val,int(cor[2])-val,int(cor[2])-val])
        mask = cv2.inRange(img,rangomin,rangomax)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cord = cv2.boundingRect(opening)
        return cord
