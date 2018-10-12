from django.urls import path, re_path
from myblog import views

app_name = 'myblog'

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('newpost/', views.newpost, name='newpost'),
    path('post/<int:pk>/', views.post_info, name='post_info')

]
