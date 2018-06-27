import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        print('[%s] : %s' % (self.client_address, '连接成功'))
        conn.sendall(bytes('欢迎来访',encoding='utf8'))
        try:
            while True:
                data = self.request.recv(1024)
                if len(data) == 0 : break
                print('[%s] says :%s'%(self.client_address,data.decode()))
                self.request.sendall(data.upper())
        except Exception as e:
                print(str(e))

if __name__=='__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',1000),Myserver)
    server.serve_forever()