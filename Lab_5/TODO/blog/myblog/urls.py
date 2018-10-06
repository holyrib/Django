from django.urls import path, re_path
from myblog import views


urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('newpost/', views.feed, name='feed')
]
