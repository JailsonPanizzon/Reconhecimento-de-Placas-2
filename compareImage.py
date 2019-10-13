import cv2


def soma_img(img1, img2):
    img1 = cv2.resize(img1, (25, 17))
    img2 = cv2.resize(img2, (25, 17))
    h = int(img1.shape[0]-2)
    l = int(img1.shape[1]-2)
    r, g, b = 0, 0, 0
    for i in range(1, h, 1):
        for j in range(1, l, 1):
            r = r + abs(img1[i][j][0]-img2[i][j][0])
            g = g + abs(img1[i][j][1]-img2[i][j][1])
            b = b + abs(img1[i][j][2]-img2[i][j][2])
    return ((r+g+b)/3)/(h*l)


i = 1
while(i <= 313):
    print(i)
    img1 = cv2.imread('teste/'+str(i)+'.jpg')
    j = i+1
    while(j <= 313):
        img2 = cv2.imread('teste/'+str(j)+'.jpg')
        if(soma_img(img1, img2) < 10):
            print('----->'+str(i)+' == ' + str(j))
        j += 1
    i += 1
