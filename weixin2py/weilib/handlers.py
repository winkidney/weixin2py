#!/usr/bin/env python
#coding:utf-8
#weilib/handlers.py - router handlers for weilib
#ver 0.1 by winkidney 2014.05.10

from .lib import text_response

def default_handler(recv_msg):
    return text_response(recv_msg, "没有匹配操作，返回默认信息")
   


