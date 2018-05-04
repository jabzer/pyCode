import socket

host = '127.0.0.1'
port = 1000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))
while True:

    msg = input('你的信息::\n').strip()
    print(msg)
    if msg=='bye':
        break
    if len(msg) ==0:continue

    s.sendall(bytes(msg,encoding='utf8'))
    data = s.recv(1024)

    print(str(data,encoding='utf8'))
print('bye')
s.close()