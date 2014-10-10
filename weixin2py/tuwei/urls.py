# coding:utf-8
# tuwei/urls.py - urls of tuwei
from django.conf.urls import patterns, include, url

from tuwei import views

from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'weixin2py.views.home', name='home'),
                       # url(r'^weixin2py/', include('weixin2py.foo.urls')),
                       url(r'^$', views.home),
                       )
