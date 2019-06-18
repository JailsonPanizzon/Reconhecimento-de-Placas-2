import os
import cv2
cont = 1
for img in os.listdir("positive"):
    im = cv2.imread("positive/"+str(img))
    print(img)
    im = cv2.resize(im,(690,720))
    cv2.imwrite("rawdata/"+str(cont)+".bmp", im)
    cont += 1
