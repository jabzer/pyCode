import os
import socket
import json

ip_port=('127.0.0.1',1000)
s = socket.socket()

s.connect(ip_port)

welcome_msg = s.recv(1024)

print("from server : ",welcome_msg.decode())

while True:
    send_data = input('put 文件路径 >>').strip()
    if len(send_data)==0:continue
    cmd_list =send_data.split()
    if len(cmd_list)<2:continue
    task_type = cmd_list[0]
    if task_type =='put':
        abs_filepath = cmd_list[1]
        if os.path.isfile(abs_filepath):
            file_size = os.stat(abs_filepath).st_size#获取文件大小
            file_name = abs_filepath.split('\\')[-1]
            print('file:{0} size:{1}'.format(abs_filepath,file_size))
            msg_data={'action':'put','file_name':file_name,'file_size':file_size}
            s.send(bytes(json.dumps(msg_data),encoding='utf-8'))

            sever_confim = s.recv(1024)
            confirm_data = json.loads(sever_confim.decode())

            if confirm_data['status']==200:
                print('开始传输文件：',file_name)
                f = open(abs_filepath,'rb')
                for line in f:
                    s.send(line)
                print('发送成功')
                continue
        else:
            print("不存在此文件:",abs_filepath)
            continue
    else:
        print('不支持此操作')
        continue
    recv_data = s.recv(1024)
    print(str(recv_data,encoding='utf-8'))
s.close()