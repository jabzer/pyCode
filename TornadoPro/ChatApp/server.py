#!/usr/bin/python3
import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")
    def post(self):
        self.write("hello,123")

def make_app():
    return tornado.web.Application([
        (r"/",IndexHandler),
    ])

if __name__ == '__main__':
    application = make_app()
    application.listen(5000)
    tornado.ioloop.IOLoop.current().start()