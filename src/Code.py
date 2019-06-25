import cv2
from detect_color import cl
cap = cv2.VideoCapture("VID-20190617-WA0009.mp4")
#cap = cv2.VideoCapture("VID-20190617-WA0010.mp4")
cascade = cv2.CascadeClassifier("cascade.xml")
while True:
    ret, img = cap.read()
    cor1 =[255,100,50]
    cor2 =[50,0,0]
    #cor1 = cl.convert2hsv([50,255,50])
    #cor2.append(cor1[0]-1)
    #cor2.append(cor1[1]-1)
    #cor2.append(20)

    cord = cl.detect(img,cor1,cor2)
    print(cor1)
    print(cor2)
    if (not(cord[0] == 0 and cord[1] == 0 and cord[2] == 0 and cord[3] == 0)):
        img = img[cord[1]:cord[1]+cord[3],cord[0]:cord[0]+cord[2]]
        placa = cascade.detectMultiScale(img, 1.3,5)
        print(cord)
        for (x,y,w,h) in placa:
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("shown",img)
    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break
