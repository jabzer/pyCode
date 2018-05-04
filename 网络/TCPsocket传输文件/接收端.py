import socket, struct

host = '127.0.0.1'
port = 1000

fmt = '128si'
recv_buffer = 4096

listenSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSock.bind((host, port))

while True:
    print('启动接收端...')
    listenSock.listen(5)
    conn, addr = listenSock.accept()
    headsize = struct.calcsize(fmt)
    head = conn.recv(headsize)
    filename = struct.unpack(fmt, head)[0].decode().rstrip('\0')
    filename = 'tmp\\' + filename
    filesize = struct.unpack(fmt, head)[1]
    print("文件名: {0} --文件大小: {1}".format(filename, str(filesize)))
    recved_size = 0
    fd = open(filename, 'wb')
    count = 0
    while True:
        data = conn.recv(recv_buffer)
        recved_size = recved_size + len(data)
        fd.write(data)
        if recved_size == filesize:
            break
    fd.close()
    print('{0} 文件传输成功'.format(filename))
