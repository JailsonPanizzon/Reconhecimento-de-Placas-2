import cv2

class cl:
    def detect(img,cor):
        kernel = np.ones((5 , 5), np.uint8)
        cord=[]
        cord.append([0,0])
        cord.append([1,1])
        val = 30
        rangomax = np.array([int(cor[0])+val,int(cor[1])+val,int(cor[2])+val])
        rangomin = np.array([int(cor[2])-val,int(cor[2])-val,int(cor[2])-val])
        mask = cv2.inRange(img,rangomin,rangomax)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cord = cv2.boundingRect(opening)
        return cord
