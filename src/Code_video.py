import cv2
import os
from detect_color import cl

cap = cv2.VideoCapture("avaliacao_videos/video01.mp4")
#cap = cv2.VideoCapture("avaliacao_videos/video02.mp4")
#cap = cv2.VideoCapture("avaliacao_videos/video03.mp4")

cascade = cv2.CascadeClassifier("cascade.xml")
cont = 0
contp=0
while True:
    ret, img = cap.read()
    cor1 =[255,200,200]
    cor2 =[60,0,0]
    img = cl.equaliza(img)
    #img = cl.detect(img,cor1,cor2)
    tam = (int(img.shape[0]*0.6),int(img.shape[1]*0.4))
    placa = cascade.detectMultiScale(img,2.9,9,0,tam)
    cv2.imshow("show",img)
    print("========================================")    
    for (x,y,w,h) in placa:
        yh,yh2,xh,xh2 = y,y+h,x,x+w
        p = 0.4
        if(y-(h*p) > 0):
            yh = int(y-(h*p))
        if(y+(h*p) < img.shape[0]-1):
            yh2 = int(y+h+(h*p))
        if(x-(w*p) > 0):
            xh = int(x-(w*p))
        if(x+(w*p) < img.shape[1]-1):
            xh2 = int(x+w+(w*p))
        img = img[yh:yh2,xh:xh2]
        if(img.shape[0]>0 and img.shape[1] > 0 ):
            contp+=1
            cont+=1
            cv2.imwrite("results/video/"+str(cont)+".png",img)
            text = (cl.readText(img))
            if(len(text) < 4 and contp > 5):
                contp = 0
                os.system("espeak -vpt 'Placa de perigo detectada conteudo ilegivel'")
            else:
                os.system("espeak -vpt '"+text+"'")
            print(text)
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),1)
            cv2.imshow("shown",img)
        
    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break
