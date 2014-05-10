#!/usr/bin/env python
#coding:utf-8
#WeiLib/handlers.py - router handlers for WeiLib
#ver 0.1 by winkidney 2014.05.10

import re
from WeiLib.handlers import default_handler


def file_router(router_patterns, recv_msg):
    for type,key,handler in router_patterns:
        if recv_msg.msg_type == 'text':
            match = re.search(key, recv_msg.content)
            if match:
                return handler(recv_msg)
            else: 
                return default_handler(recv_msg)
        elif recv_msg.msg_type == type:
            return handler(recv_msg)
        return default_handler(recv_msg)
    
def db_router(recv_msg):
    pass

 