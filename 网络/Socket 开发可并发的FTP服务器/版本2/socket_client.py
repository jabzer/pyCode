import socket
ip_port =('127.0.0.1',1000)

s= socket.socket()
s.connect(ip_port)
welcome_msg = s.recv(1024)
print("from server : " ,welcome_msg.decode())

while True:
    send_data = input(">>").strip()
    if len(send_data)==0:continue
    s.send(bytes(send_data,encoding='utf8'))
    recv_data = s.recv(1024)
    print(str(recv_data,encoding='utf8'))

s.close()