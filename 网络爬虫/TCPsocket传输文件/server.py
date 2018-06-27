import socket, os, struct

host = '127.0.0.1'
port = 1000
fmt = '128si'
send_buffer = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

filepath = input("enter file path:")
filename = os.path.split(filepath)[1]
print(filename)
filesize = os.path.getsize(filepath)
print("文件名: {0} --文件大小: {1}".format(filename, str(filesize)))
head = struct.pack(fmt, filename.encode(), filesize)
print('\n 头文件大小:' + str(head.__len__()) + '\n' + str(head))
sock.sendall(head)
restSize = filesize

fd = open(filepath, 'rb')
count = 0
while restSize >= send_buffer:
    data = fd.read(send_buffer)
    sock.sendall(data)
    restSize = restSize - send_buffer
    print(str(count) + " ")
    count = count + 1
data = fd.read(restSize)
sock.sendall(data)
fd.close()
print('发送成功!' + filename)
