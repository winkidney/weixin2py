#coding:utf-8
#in folder 'pycms'
#session classes by winkidney,used to store session status
import datetime
class WeiSession(object):
    '''微信助手会话类，用来存储用户的会话状态'''
    def __init__(self):
        self.start_time = datetime.datetime
        self.status = ''
    def menu_up(self):
        self.status = self.status[0:-2]
    def menu_add(self,menu_obj):
        self.status = self.status+menu_obj
class WeiChatSession(object):
    pass