#!/usr/bin/env python
# coding:utf-8
# tuwei/handlers.py - router handlers for tuwei
# ver 0.1 by winkidney 2014.05.10
from weilib.lib import PTItem
from weilib.lib import text_response, pic_text_response


def test_handler(recv_msg, *args, **kwargs):
    title = "测试图文消息"
    description = "图文消息描述"
    pic_url = "http://blog.gg-workshop.com/static/upload/201405/665d5190-d9af-11e3-a9aa-04010628bc01.png"
    url = "http://blog.gg-workshop.com"
    items = []
    items.append(PTItem(title, description, pic_url, url))
    items.append(PTItem(title, description, pic_url, url))
    return pic_text_response(recv_msg, items)


def about_handler(recv_msg, *args, **kwargs):
    content = """
    关于我们
    """
    return text_response(recv_msg, content)


def subscrib_handler(recv_msg, *args, **kwargs):
    content = """
    --键入小写命令--
    view   查看活动
    input  发起活动
    help   帮助信息
    about  关于我们
    使用相应功能^_^
    """
    return text_response(recv_msg, content)


def help_handler(recv_msg, *args, **kwargs):
    return subscrib_handler(recv_msg, *args, **kwargs)
