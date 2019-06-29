import cv2
import numpy as np
from PIL import Image
from matplotlib import cm
import pytesseract


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
        cv2.imshow("cor", mask)
        return mask

    '''def convert2hsv(rgb):
        hsv=colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
        return hsv

    def convert2rgb(hsv):
        rgb = colorsys.hsv_to_rgb(hsv[0],hsv[1],hsv[2])
        return rgb'''

    def equaliza(img):
        #equaliza imagens nos canais R,G,B
        b, g, r = cv2.split(img)
        red = cv2.equalizeHist(r)
        green = cv2.equalizeHist(g)
        blue = cv2.equalizeHist(b)
        blue=b
        return cv2.merge((blue, green, red))
    
    def readText(img):
        #pytesseract.pytesseract.tesseract_cmd = ( r"C:\Program Files (x86)\Tesseract")
        cv2.imwrite("t1.bmp",img)
        im = Image.open("t1.bmp")
        phrase = pytesseract.image_to_string((im), lang="eng")
        return phrase
