"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include,url
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('feedback',views.feedback,name='feedback'),
    path('passw',views.passw,name='passw'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('search', views.search, name='search'),
    path('studentlog',views.studentlog,name="studentlog"),
    path('proflog',views.proflog,name="proflog"),
    path('addprof',views.addprof,name='addprof'),
    path('addstud',views.addstud,name='addstud'),
    path('profsign',views.profsign,name='profsign'),
    path('studsign',views.studsign,name='studsign'),
    path('delete',views.delete,name='delete'),
    path('delobj',views.delobj,name='delobj'),
    path('check',views.check,name="check"),
    path('changep',views.changep,name="changep"),
    path('list',views.list,name="list"),

]
