import urllib
#from urllib.request import urlopen
import numpy as np
import cv2
import os
import subprocess
def montar_negativas():
    link_imagens_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03215508'
    urls_imagens_negativas = urllib.request.urlopen(link_imagens_negativas).read().decode()


    if not os.path.exists('negatives'):
        os.makedirs('negatives')

    nmr_imagem=1

    for i in urls_imagens_negativas.splitlines():
        try:
            urllib.request.urlretrieve(i,str(nmr_imagem)+".jpg")
            img = cv2.imread(str(nmr_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)
            img_redimin=cv2.resize(img,(640,480))
            cv2.imwrite(str(nmr_imagem)+".jpg",img_redimin)
            nmr_imagem+=1
        except Exception as e:
            print(str(e))
def gera_list_neg():
        for img in os.listdir():
	    line = "negativas"
            line += img+'\n'
            with open('bg.txt','a') as f:
                f.write(line)
#montar_negativas()
gera_list_neg()
