#!/usr/bin/env python
#coding:utf-8
#tuwei/tests.py - test file of the lib
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from WeiLib.lib import create_menu,MButton
from django.template.loader import render_to_string

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

def create_btns(token):
    btn1 = MButton('活动相关')
    btn2 = MButton('我来组织')
    btn3 = MButton('关于我们')
    m_list = [btn1, btn2, btn3]
    
    btn1.add_button(MButton('即将进行', key='GET_CURRENT_ACTIVITY'))
    btn1.add_button(MButton('活动历史', key='GET_ACTIVITY_HISTORY'))
    btn1.add_button(MButton('活动报名', key='SIGN_FOR_ACTIVITY'))
    
    btn2.add_button(MButton('发起活动', url='http://wwww.baidu.com'))
    btn2.add_button(MButton('为活动投票',key='VOTE_FOR_ACTIVITY'))
    
    btn3.add_button(MButton('突围俱乐部', key='ABOUT_TUWEI'))
    btn3.add_button(MButton('组织者们', key='ABOUT_AUTHORS'))
    btn3.add_button(MButton('核心价值观', key='CORE_VALUES'))
    btn3.add_button(MButton('联系我们', key='CONTACT_US'))

    return m_list


    
    
    
    
    