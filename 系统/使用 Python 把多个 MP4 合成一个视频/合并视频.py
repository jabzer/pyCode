from moviepy.editor import *
from natsort import natsorted
import os

type = '.flv'


def Combining(baseDir):
    L = []
    for root, dirs, files in os.walk(baseDir):
        files = natsorted(files)
        for file in files:
            if os.path.splitext(file)[1] == type:
                filePath = os.path.join(root, file)
                print(filePath)
                video = VideoFileClip(filePath)
                print(video)
                L.append(video)
    final_clip = concatenate_videoclips(L)
    final_clip.write_videofile(baseDir+"\\target.mp4", fps=24, remove_temp=False)


if __name__ == "__main__":
    baseDir = "D:\\迅雷下载\\10376670\\1"
    Combining(baseDir)
