import json
import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print('[%s] : %s' % (self.client_address, '连接成功'))
        self.request.sendall(bytes('欢迎欢迎热烈欢迎',encoding='utf-8'))
        while True:
            data = self.request.recv(1024)
            if len(data)==0:break
            print('[%s] 说 :%s' % (self.client_address, data.decode()))
            task_data = json.loads(data.decode())
            print(task_data)
            task_action = task_data.get("action")
            print(task_action)
            if hasattr(self,"task_%s"%task_action):
                func = getattr(self,"task_%s"%task_action)
                func(task_data)
            else:
                print('task action is not support',task_action)
    def task_put(self,*args,**kwargs):
        print('--put',args,kwargs)
        file_size = args[0].get('file_size')
        file_name = args[0].get('file_name')

        server_reponse = {"status":200}
        self.request.send(bytes(json.dumps(server_reponse),encoding='utf-8'))
        f = open(file_name,'wb')
        recv_size =0
        while recv_size<int(file_size):
            data = self.request.recv(4096)
            f.write(data)
            recv_size+=len(data)
        print("文件接收成功")
        f.close()


if __name__=='__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',1000),Myserver)
    print("启动服务")
    server.serve_forever()