from django.urls import path, re_path
from main import views


urlpatterns = [
    path('', views.index),
    path('todo/', views.todo, name='todo'),
    path('todo/1/completed',views.todo_completed),
    path('done_task/<task_id>', views.done_task, name="done_task"),
]
