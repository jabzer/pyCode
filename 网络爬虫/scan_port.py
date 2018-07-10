#!/usr/bin/python3
import sys,threading,socket

lock = threading.Lock()

openNum = 0
threads = []

def socketPort(ip,port):
    '''传入ip/port'''
    try:
        global openNum
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = server.connect_ex((ip,port))
        lock.acquire()
        if  result == 0:
            openNum+=1
            print('Scan %s Port %d:OPEN'%(ip,port))
        lock.release()
        server.close()
    except:
        pass

def threadScan(ip,port_list):
    for p in port_list:
        t = threading.Thread(target=socketPort,args=(ip,p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('[+++] scan is complete!')
    print('[+++] 一共开启了 %d'%(openNum))






if __name__ == '__main__':
    ip = '207.148.92.20'
    port_list = [21, 22, 23, 25, 80, 135, 137, 139, 445, 1433, 3306, 3389, 8000,55555]#定义端口列表
    print('[+++] 扫描开始')
    threadScan(ip,port_list)