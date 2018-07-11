# -*- coding: utf-8 -*-
import os
from PIL import Image

dir='E:\\签名图片\\'
newdir='E:\\签名图片\\01\\'
for root,dirs,files in os.walk(dir,topdown=True):
    for file in files:
        if 'jpg' in file:
            print('打开:'+os.path.join(root,file))
            jepg=Image.open(os.path.join(root,file))
            s=newdir+file.replace('.jpeg','.jpg').replace('.png','.jpg').replace('.tif','.jpg').replace('.JPG','.jpg').replace('.JPEG','.jpg')
            s=s.replace('.jpg','.bmp')
            print(s)
            #jepg.save(s, quality=100)
            new_img=jepg.resize((168,70),Image.ANTIALIAS)
            new_img.save(s,quality=1)

input("按任意键结束...")
