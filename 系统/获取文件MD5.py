#!/usr/bin/python3
import sys,os,hashlib

def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print(hash)
        return hash


if __name__ == '__main__':
    if len(sys.argv)==2:
        hashfile = sys.argv[1]
        if not os.path.exists(hashfile):
            hashfile = os.path.join(os.path.dirname(__file__),hashfile)
            if not os.path.exists(hashfile):
                print("cannot found file")
            else:
                CalcMD5(hashfile)
        else:
            CalcMD5(hashfile)
    else:
        print("no filename")