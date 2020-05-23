from django.urls import path,include,re_path
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

"""
From DJRF tutorial 3, Class based views
"""
app_name = 'aws'

urlpatterns = [
    path('',views.index,name='index'),
    ]
