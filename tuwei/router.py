#!/usr/bin/env python
#coding:utf-8
#tuwei/router.py - message router to generate response message
#ver 0.1 by winkidney 2014.05.10

import re

from tuwei.handlers import help_handler



router_patterns =[
         # 消息类型  消息文字（非文字类型消息留空）  操作函数
         ('text',re.compile('^帮助$'),help_handler),
         ]

