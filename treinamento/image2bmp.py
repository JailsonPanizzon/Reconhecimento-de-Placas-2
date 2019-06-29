import os
import cv2
import PIL
from PIL import ImageFilter
from PIL import Image
import numpy

def invert(im):    
    i=1
    while i<im.shape[0]:
        j=1
        while j<im.shape[1]/2:
            aux = im[i][j].copy()
            im[i][j] = im[i][im.shape[1]-j]
            im[i][im.shape[1]-j]= aux
            j+=1
        i+=1
    return im

cont = 277
for img in os.listdir("positive"):
    im = cv2.imread("positive/"+str(img))
    print(cont)
    im = cv2.resize(im,(690,720))
    im = invert(im)
    cv2.imwrite("rawdata/"+str(cont)+".bmp", im)
    cont += 1
    




