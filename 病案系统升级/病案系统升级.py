# -*- coding: utf-8 -*-
# 先拷贝配置文件，版本号不对就通过FTP下载新文件夹，版本号对就直接启动程序
import os, ftplib, configparser, shutil

f = ftplib.FTP('10.11.0.10')
f.login()

def ftpconnect(host='10.11.0.10'):
    f = ftplib.FTP(host)
    f.login()
    print('{0} connect success'.format(host))
    return f


def downLoadFile(ftp,loaclpath,remotepath):
    fp = open(loaclpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write)
    # ftp.set_debuglevel(0)
    fp.close()


def downloaddir(localdir, remotedir):
    if not os.path.exists(localdir + remotedir):
        os.mkdir(localdir + remotedir)
    try:
        f.cwd(remotedir)
    except:
        print("目录不存在")
        return
    print('切换到目录 %s'% f.pwd())



def readConfig(file, selection, key):
    config = configparser.ConfigParser()
    config.read(file, 'gbk')
    result = ""
    try:
        result = config.get(selection, key)
    except Exception as e:
        print("错误:{0}".format(str(e)))
    return result


def setConfig(file, selection, key, vaule):
    config = configparser.ConfigParser()
    config.read(file, 'gbk')
    try:
        config.set(selection, key, vaule)
        config.write(open(file, 'w'))
    except Exception as e:
        print("错误:{0}".format(str(e)))
    return 0


if __name__ == '__main__':
    # 建立文件夹
    localdir = "D://病案管理"
    os.makedirs(localdir, exist_ok=True)
    # 下载远程ini文件
    ftp = ftpconnect()
    downLoadFile(ftp, localdir + '//server.ini', 'server.ini')
    # 读取配置
    localfile = localdir + '//local.ini'
    if not os.path.exists(localfile):
        shutil.copy(localdir + '//server.ini', localfile)
        setConfig(localfile, 'Version', 'version', '0')
    host = readConfig(localfile, 'ftpconf', 'host')
    remote = readConfig(localfile, 'ftpconf', 'filespath')
    version_local = readConfig(localfile, 'Version', 'version')

    version_server = readConfig(localdir + '//server.ini', 'Version', 'version')
    print('host:{0};remte:{1};version_local:{2};version_server:{3}'.format(host, remote, version_local, version_server))
    if version_local != version_server:
        # 下载文件
        #downloaddir(ftp, localdir, remote)
        pass
        # 更改版本号
        # setConfig(localfile, 'Version', 'version', version_server)
