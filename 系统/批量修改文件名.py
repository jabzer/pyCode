import os

path = "C:\\Users\\Jabzer\\Downloads\\恐怖熱線"

def mp4Tomp3(path):
    for root,dirs,files in os.walk(path,topdown=True):
        for i in files:
            oldname = root+'\\'+i
            if os.path.splitext(root+'\\'+i)[1] == '.mp4':
                newname = os.path.splitext(root+'\\'+i)[0]+'.mp3'
                os.rename(oldname,newname)
                print(oldname + "--------》"+newname)

def mp3Tomp4(path):
    for root,dirs,files in os.walk(path,topdown=True):
        for i in files:
            oldname = root+'\\'+i
            if os.path.splitext(root+'\\'+i)[1] == '.mp3':
                newname = os.path.splitext(root+'\\'+i)[0]+'.mp4'
                os.rename(oldname,newname)

mp4Tomp3(path)