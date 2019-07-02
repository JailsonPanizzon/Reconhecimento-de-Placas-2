import cv2
import os
from detect_color import cl


cascade = cv2.CascadeClassifier("cascade.xml")
cont = 0
contp=0
for i in os.listdir("avaliacao"):
    img = cv2.imread("avaliacao/"+str(i)) 
    cor1 =[255,200,200]
    cor2 =[60,0,0]
    img = cl.equaliza(img)
    #img = cl.detect(img,cor1,cor2)
    tam = (int(img.shape[0]*0.5),int(img.shape[1]*0.2))
    placa = cascade.detectMultiScale(img,1.1,5,0,tam)
    
    print("========================================")    
    for (x,y,w,h) in placa:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),1)
        yh,yh2,xh,xh2 = y,y+h,x,x+w
        p = 0.5
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
            cv2.imshow("shown",img)
            contp+=1
            cont+=1
            cv2.imwrite("results/images/"+str(cont)+".png",img)
            text = (cl.readText(img))
            os.system("espeak -vpt '"+text+"'")
            print(text)
    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break
