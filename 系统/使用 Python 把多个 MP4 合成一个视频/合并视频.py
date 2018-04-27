from moviepy.editor import *
from natsort import natsorted
import os

type = '.flv'


def Combining(baseDir):
    print("开始合并:{0}".format(baseDir))
    L = []
    for root, dirs, files in os.walk(baseDir):
        files = natsorted(files)
        for file in files:
            if os.path.splitext(file)[1] == type:
                filePath = os.path.join(root, file)
                video = VideoFileClip(filePath)
                print("加载文件："+filePath)
                L.append(video)
    if len(L) > 0:
        final_clip = concatenate_videoclips(L)
        print("加载完成！\n 开始合并视频...\n")
        final_name = "_".join(baseDir.split('\\')[-2:])
        final_clip.write_videofile(baseDir + "\\{0}.mp4".format(final_name), fps=24, remove_temp=True)
        print("完成：合并目录{0}视频")
    else:
        print("此目录没有{0}文件。".format(type))


if __name__ == "__main__":
    path = "E:\\教程\\哔哩哔哩"
    for root, dirs, files in os.walk(path):
        if not dirs:
            print('root : {0}'.format(root))
            Combining(root)
    # baseDir = "D:\\迅雷下载\\10376670\\1"
    # Combining(baseDir)
