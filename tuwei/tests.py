#!/usr/bin/env python
#coding:utf-8
#tuwei/tests.py - test file of the lib
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from WeiLib.lib import create_menu,MButton,get_token
from django.template.loader import render_to_string

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

def create_btns():
    btn1 = MButton('过往活动')
    btn2 = MButton('活动')
    btn3 = MButton('我们')
    m_list = [btn1, btn2, btn3]
    
    btn1.add_button(MButton('智能硬件', key='VIEW_SMART_HARDWARE'))
    btn1.add_button(MButton('移动互联', key='VIEW_MOBILE_COMMUNICATION'))
    btn1.add_button(MButton('技能互换', key='VIEW_SKILL_SWAP'))
    btn1.add_button(MButton('户外', key='VIEW_OUTDOOR'))
    
    btn2.add_button(MButton('近期活动', url='http://weixin2py.gg-workshop.com/recent/'))
    btn2.add_button(MButton('技能互换', url='http://weixin2py.gg-workshop.com/recent/'))
    btn2.add_button(MButton('我来组织',key='CREATE_ACTIVITY'))
    
    btn3.add_button(MButton('微信功能', key='ABOUT_WEIXIN'))
    btn3.add_button(MButton('了解突围', key='ABOUT_TUWEI'))
    btn3.add_button(MButton('成员介绍', key='ABOUT_MEMBERS'))
    btn3.add_button(MButton('加入我们', key='JOIN_US'))

    return m_list

def post_menu(appid, appsecret):
    mlist = create_btns
    token = get_token(appid, appsecret)
    create_menu(token, mlist)
    
    
    
    
    
    