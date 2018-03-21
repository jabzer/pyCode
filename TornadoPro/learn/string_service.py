# -*- coding: utf-8 -*-
import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        greeting = self.get_argument('name','Hello')
        self.write(greeting+',friendly user!')

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input,*args, **kwargs):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        text = self.get_argument('text')
        width = self.get_argument('width',20)
        self.write(textwrap.fill(text,int(width)))

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/",IndexHandler),
            (r"/reversr/(\w+)",ReverseHandler),
            (r"/wrap",WrapHandler),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()