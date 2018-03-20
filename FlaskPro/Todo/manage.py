from todo import todo
from todo.models import Todo
from flask_script import Manager

manager =  Manager(todo)

@manager.command
def save():
    todo = Todo(content='测试1')
    todo.save()

if __name__=='__main__':
    manager.run()