# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url

from .views import (
    TodoListApiView,
    TodoDetailApiView,
)

urlpatterns = [
     url('api', TodoListApiView.as_view(), name='todo'),
      path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]
