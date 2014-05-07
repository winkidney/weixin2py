#coding:utf-8
#/core/lib.py - contains some tool function 
# kidney 2014.5.20

from django.contrib.auth.models import User
from core.models import WeixinUser,WeixinUserProfile


def create_new_user(received_msg):
    """create a new user contains user profile by received openid"""
    weixin_user = WeixinUser()
    weixin_user.openid = received_msg.from_user_name
    weixin_user.gouda_off = True
    weixin_user.is_bind = False
    weixin_user.auth_user_id = 1
    
    weixin_user.profile = user_profile
    user = User.objects.create_user(weixin_user.openid,'default@qq.com',weixin_user.openid)
    user.save()
    weixin_user.auth_user = user
    weixin_user.save()
    
def user_exist(received_msg):
    try:
        WeixinUser.objects.get(openid=received_msg.from_user_name)
        return True
    except :
        return False
def bind_user(recevied_msg):
    pass