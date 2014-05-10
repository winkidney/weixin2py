#!/usr/bin/env python
#coding:utf-8
#tuwei/handlers.py - router handlers for tuwei
#ver 0.1 by winkidney 2014.05.10
from WeiLib.lib import text_response

def help_handler(recv_msg):
    return text_response(recv_msg, "发送信息，我也是醉了")