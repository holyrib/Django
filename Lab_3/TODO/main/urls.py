from django.urls import path, re_path
from main import views


urlpatterns = [
    path('', views.index),
    path('todo/', views.todo),
    path('todo/1/completed',views.todo_completed)
]
