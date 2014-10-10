#!/usr/bin/env python
# coding:utf-8
# tuwei/router.py - message router to generate response message
# ver 0.1 by winkidney 2014.05.10

import re

from .handlers import (help_handler, about_handler,
                            test_handler)


"""
参考信息：
消息类型：text ,event,image, video, link , location,
"""
router_patterns = [
    # 消息类型  消息文字（非文字类型消息留空）  操作函数
    #('text', re.compile('^help$'), help_handler),
    #('text', re.compile('^about$'), about_handler),
    #('text', re.compile('^test$'), test_handler),
]
