'''
Created on 22-Nov-2016

@author: sachin
'''
from django.conf.urls import url
from blog import views
urlpatterns=[
             url(r'^$', views.post_list, name='post_list'),
             url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
             ]