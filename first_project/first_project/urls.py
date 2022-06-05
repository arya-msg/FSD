"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("tictactoe/", views.tictactoe, name ='tictactoe'),
    path("wordle/", views.wordle, name ='wordle'),
    path("project5_6/", views.load_project5_6, name ='project56'),
    path("project5_6/help", views.help, name ='project56_help'),
    path("project7_8/", views.load_project7_8, name ='project78'),
    # path("project9/", views.load_project7_8, name ='project9'),
    path('project7_8/degree/', views.add_degree,  name='adddegree'),
    path('project7_8/student/', views.add_student,  name='addstudent'),
    # path('get_student/', views.get_student,  name='student'),
    path("project7_8/student/search/", views.search_student, name ='search_student'),


]
