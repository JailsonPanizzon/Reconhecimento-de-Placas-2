import os
import cv2
from detect_color import cl
for img in os.listdir("rawdata"):
    im = cv2.imread("rawdata/"+str(img))
    print(img)
    cor1 =[255,200,200]
    cor2 =[60,0,0]
    im = cl.equaliza(im)
    im = cl.detect(im,cor1,cor2)
    cv2.imwrite("rawdata/"+img, im)
