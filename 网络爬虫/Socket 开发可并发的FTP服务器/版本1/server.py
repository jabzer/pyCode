import socket

host = '127.0.0.1'
port = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('连接成功' + str(addr))
    while True:
        print('-')
        data = conn.recv(1024)
        print(str(data, encoding='utf8'))
        if not data:
            print('断开连接' + str(addr))
            break
        conn.sendall(data.upper())

    conn.close()
    print('关闭连接' + str(addr))

