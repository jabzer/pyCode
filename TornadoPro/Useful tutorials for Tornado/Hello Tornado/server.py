# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        messages = ["one","two"]
        self.render("index.html",messages=messages)
    def post(self, *args, **kwargs):
        self.write("post tornado")

if __name__=="__main__":
    application = tornado.web.Application(
        [
            (r"/",IndexHandler),
        ],autoreload=True,compiled_template_cache=False
    )
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()