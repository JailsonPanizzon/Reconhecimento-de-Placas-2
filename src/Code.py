import cv2
from detect_color import cl
#cap = cv2.VideoCapture("VID-20190617-WA0009.mp4")
cap = cv2.VideoCapture("VID-20190617-WA0010.mp4")
cascade = cv2.CascadeClassifier("cascade.xml")
while True:
    ret, img = cap.read()
    placa = cascade.detectMultiScale(img, 1.9,5)
    print(cl.detect(img,255))
    for (x,y,w,h) in placa:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("shown",img)
    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break
