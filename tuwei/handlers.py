#!/usr/bin/env python
#coding:utf-8
#tuwei/handlers.py - router handlers for tuwei
#ver 0.1 by winkidney 2014.05.10
from WeiLib.lib import text_response


def about_handler(recv_msg, *args, **kwargs):
    content = """
我们叫突围俱乐部。针对白领阶层,工作之余进行交流,组织很多有趣的活动。
分布式管理,每个参与者也可以是组织者,只要组织者组织的活动引起大家的兴趣与参与,并且确保安全与合法的情况下都可以组织活动。
    """
    return text_response(recv_msg, content)

def subscrib_handler(recv_msg, *args, **kwargs):
    content = """键入命令
    view   查看活动
    input  发起活动
    help   帮助信息
    about  关于我们
    使用相应功能^_^
    """
    return text_response(recv_msg, content)

def help_handler(recv_msg, *args, **kwargs):
    return subscrib_handler(recv_msg, *args, **kwargs)
   