from flask import Flask
from flask_mongoengine import MongoEngine

todo = Flask(__name__)
todo.config.from_object('config')

db = MongoEngine(todo)

from todo import views,models