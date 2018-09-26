from django.shortcuts import render
from django.http import HttpResponse
from .forms import Taskform
from .models import Task

import datetime


def index(request):

    return HttpResponse('<h3>HI! I am working!<h3>')


# def todo(request):
#     tasks = ['do lab 3', 'sleep', 'eat', 'breath', 'running']
#     created = datetime.datetime.now()
#     due = datetime.datetime.now()
#     todo_list = {
#         'tasks': tasks,
#         'created': created,
#         'due': due,
#         'owner': 'Admin',
#         'status': 'Done'
#     }
#
#     return render(request, 'todo_list.html', todo_list)


def todo(request):

    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            post.save()
            return render(request, 'todo_list.html', {'form': form})
    else:
        form = Taskform()
        tasks = Task.objects.all()
        args = {'form': form, 'tasks' : tasks}
        return render(request, 'todo_list.html', args)


def todo_completed(request):
    tasks = ['lab 1', 'lab 2', 'Watch new episode']
    created = datetime.datetime.now() - datetime.timedelta(days=3)
    due = datetime.datetime.now() - datetime.timedelta(days=1)
    done = {
        'tasks': tasks,
        'created': created,
        'due': due,
        'owner': 'Admin',
        'status': 'Not done'
    }
    return render(request, 'completed_todo_list.html',done)