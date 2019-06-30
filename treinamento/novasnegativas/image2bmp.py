import os
import cv2
cont = 203
for img in os.listdir("web2"):
    im = cv2.imread("web2/"+str(img))
    print(img)
    im = cv2.resize(im,(640,480))
    im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("new/"+str(cont)+".jpg", im)
    cont += 1
