import cv2
import numpy as np
from PIL import Image
import colorsys

class cl:
    def detect(img,cor1,cor2):
        '''im2 = Image.new('RGB',(280,280),(255,255,255))
        im2.save('img.png')
        im = cv2.imread('img.png')
        im2 =cv2.imread('img.png')
        i=0
        while(i<279):
            j=0
            while(j<279):
                im[i][j] = cor1
                im2[i][j]=cor2
                j+=1
            i+=1
        cv2.imwrite("imgfg.png",im2)
        cv2.imwrite("img.png",img)'''
        kernel = np.ones((5 , 5), np.uint8)
        cord = []
        rangomax = np.array([int(cor1[2]),int(cor1[1]),int(cor1[0])])
        rangomin = np.array([int(cor2[2]),int(cor2[1]),int(cor2[0])])
        mask = cv2.inRange(img,rangomin,rangomax)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cord = cv2.boundingRect(opening)
        x, y, w, h = cv2.boundingRect(opening)
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x+w, y + h), (255, 255, 0), 5)
        cv2.imshow("cor", mask)
        return cord

    def convert2hsv(rgb):
        hsv=colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
        return hsv

    def convert2rgb(hsv):
        rgb = colorsys.hsv_to_rgb(hsv[0],hsv[1],hsv[2])
        return rgb
