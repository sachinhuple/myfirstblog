'''
Created on 22-Nov-2016

@author: sachin
'''
from django.conf.urls import url
from . import views
urlpatterns=[
             url(r'^$', views.post_list, name='post_list'),
             ]