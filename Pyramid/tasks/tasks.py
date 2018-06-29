#!/usr/bin/python3
import os, logging, sqlite3
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.events import subscriber, NewRequest, ApplicationCreated
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from wsgiref.simple_server import make_server

# 配置日志记录方式，把当前目录设为根目录
logging.basicConfig()
log = logging.getLogger(__name__)
here = os.path.dirname(os.path.abspath(__file__))


# 初始化数据库
@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    log.warn('初始化数据库...')
    with open(os.path.join(here, 'schema.sql')) as f:
        stmt = f.read()
        settings = event.app.registry.settings
        db = sqlite3.connect(settings['db'])
        db.executescript(stmt)


# 数据请求
@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    settings = request.registry.settings
    request.db = sqlite3.connect(settings['db'])
    request.add_finished_callback(close_db_connection)


def close_db_connection(request):
    request.db.close()


# 路由
@view_config(route_name='hello')
def hello():
    return Response('<body>Visit <a href="/howdy">hello</a></body>')


if __name__ == '__main__':
    # 配置选项设置
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['db'] = os.path.join(here, 'tasks.db')
    # 会话配置
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    # 加载配置
    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_route('hello', '/')
    config.scan()
    # 启动应用
    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
