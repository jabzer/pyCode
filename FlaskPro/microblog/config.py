#!/usr/bin/python3
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'sdhfiusdhfvsdjoij!@@@#@$#$#$#'
    SECRET_KEY = os.urandom(64)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
