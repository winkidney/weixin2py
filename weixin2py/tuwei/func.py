#coding:utf-8
#/core/lib.py - contains some tool function 
# kidney 2014.5.20

from django.contrib.auth.models import User
from tuwei.models import WeixinUser


def create_new_user(openid):
    
    """create a new user contains user profile by received openid
       
    """
    
    user = User.objects.create_user(weixin_user.openid,'default@qq.com',weixin_user.openid)
    user.save()
    weixin_user = WeixinUser()
    weixin_user.openid = openid
    
    weixin_user.auth_user = user
    weixin_user.save()
    
def user_exist(openid):
    try:
        WeixinUser.objects.get(openid=openid)
        return True
    except :
        return False
