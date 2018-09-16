from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):

    return HttpResponse('<h3>HI! I am working!<h3>')


def todo(request):
    tasks = ['do lab 3', 'sleep', 'eat', 'breath', 'running']
    created = datetime.datetime.now()
    due = datetime.datetime.now()
    todo_list = {
        'tasks': tasks,
        'created': created,
        'due': due,
        'owner': 'Admin',
        'status': 'Done'
    }

    return render(request, 'todo_list.html', todo_list)

def todo_completed(request):
    tasks = ['lab 1', 'lab 2', 'Watch new episode']
    created =  datetime.datetime.now() - datetime.timedelta(days = 3)
    due = datetime.datetime.now() - datetime.timedelta(days = 1)
    done = {
        'tasks': tasks,
        'created': created,
        'due': due,
        'owner': 'Admin',
        'status': 'Not done'
    }
    return render(request, 'completed_todo_list.html',done)