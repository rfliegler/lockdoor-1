from django.urls import path,include,re_path
from django.conf.urls import url
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

"""
From DJRF tutorial 3, Class based views
"""
app_name = 'aws'

urlpatterns = [
    path('',views.index,name='index'),
    ]
