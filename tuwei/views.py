#coding:utf-8
#tuwei/views.py
#django模块导入
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
import hashlib,re
from django.http import Http404

from WeiLib.router import base_router,db_router
from tuwei.router import router_patterns
                           
from tuwei.models import WeixinUser
from WeiLib.lib import (WeiSession,GetMsg,TextMsg,check_signature)
from WeiLib.handlers import default_handler

try:
    from weixin2py.localsettings import TOKEN
except:
    from weixin2py.settings import TOKEN
#router 必须是一个list实例
routers = [base_router, db_router]

       
@csrf_exempt  
def home(request):
    if request.method == 'GET':
        myresponse = HttpResponse()
        if check_signature(request, TOKEN):
            myresponse.write(request.GET.get('echostr'))
            return myresponse
        else:
            myresponse.write('不提供直接访问！')
            return myresponse
        
    if request.method == 'POST':
        #check_signature(request, TOKEN)
        recv_msg = GetMsg(request.body)
        for router in routers:
            result = router(recv_msg, router_patterns)
            if isinstance(result, HttpResponse):
                return result
        return default_handler(recv_msg)
        
