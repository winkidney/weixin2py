#!/usr/bin/env python
#coding:utf-8
#weilib/plugin/who_the_spy.py - 'Who is the spy' plugin for weilib
#ver 0.1 by winkidney 2014.05.10

from WeiLib.lib import WeiSession
import re


def processor(recv_msg):
    """A processor must return a dict.
       If not ,program will throw the returned result.
    """
    
    if '谁是卧底' in recv_msg.content:
        if re.search('/d'):
            session = WeiSession()
    if session.get_key('created') == 'yes':
        return session.get_key('')
    recv_msg.content
    return {'test_plugin': 'only_the test plugin output'}