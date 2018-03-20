import os,subprocess,time,threading

ippool =('10.11.129.1','192.168.199.1','10.11.80.1','10.11.81.1')


def get_ping_result(ip):
    cmd_str = "ping {0} -n 1 -w 600".format(ip)
    DETACHED_PROCESS = 0x00000008  # 不创建cmd窗口
    try:
        subprocess.run(cmd_str,creationflags=DETACHED_PROCESS,check=True) #win系统
    except subprocess.CalledProcessError as err:
        pass
    else:
        print("ip:{0}  is on".format(ip))


def find_ip(ip_prefix):
    for i in range(1,256):
        ip = '{0}.{1}'.format(ip_prefix,i)
        #threading.Thread(target=get_ping_result,args=(ip,)).start()
        get_ping_result(ip)
    print('end:'+ip_prefix)



if __name__=="__main__":
    for ip in ippool:
        ip_prefix = '.'.join(ip.split('.')[:-1])
        threading.Thread(target=find_ip,args=(ip_prefix,)).start()

