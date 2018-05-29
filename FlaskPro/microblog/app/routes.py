#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username':'不知道是什么'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html',title='home',posts = posts,user=user)