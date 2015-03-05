# coding:utf-8
from django.conf.urls import patterns, url

from . import views

from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'weixin2py.views.home', name='home'),
    # url(r'^weixin2py/', include('weixin2py.foo.urls')),
    url(r'^$', views.home),
)
