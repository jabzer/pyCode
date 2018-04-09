import time,os,re,time
from functools import wraps
from pytube import YouTube
from pathlib import Path

urls = (
    'https://www.youtube.com/watch?v=bvaGPWPzju0',
)

def download(url,local_dir):
    try:
        yt=YouTube(url)
    except Exception as e:
        print("[ERROR--    ]  {0}".format(str(e)).encode("utf-8"))
        return -1
    pattern = r'[\/.:?<>|]+'
    regex = re.compile(pattern)
    filename = regex.sub('',yt.title).replace('\'','').replace('\\','')+".mp4"
    p = Path(local_dir)
    fp = p/filename
    if fp.exists():
        print("[SKIP    ]{0}".format(filename))
        return 0
    try:
        print("[开始下载....]{0}".format(filename))
        yt.streams.filter(subtype='mp4',progressive=True).first().download(local_dir)
        print("[下载完成....]{0}".format(filename))
    except Exception as e:
        print("[ERROR    ]  {0}".format(str(e)).encode("utf-8"))
        return -1
    return 1

if __name__=='__main__':
    local_dir = os.path.join(os.getcwd(),"youtube")
    try:
        os.makedirs(local_dir,exist_ok=True)
    except OSError as e:
        print(e.reason)
        exit(1)

    for url in urls:
        print("[开始  ]{0}".format(url))
        ret = download(url,local_dir)
        if ret>0:
            print(re)
