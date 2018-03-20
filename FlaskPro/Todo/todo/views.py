from todo import todo
from flask import render_template,request
from .models import Todo,TodoForm
from datetime import datetime

@todo.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html',todos=todos,form=form)

@todo.route('/add',methods=['POST',])
def add():
    form = TodoForm(request.form)
    if form.validate():
        content= form.content.data
        todo = Todo(content=content,time=datetime.now())
        todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html',todos=todos,form=form)

@todo.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm(request.form)
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html',todos=todos,form=form)

@todo.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm(request.form)
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html',todos=todos,form=form)

@todo.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm(request.form)
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html',todos=todos,form=form)