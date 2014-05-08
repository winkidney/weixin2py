#coding:utf-8
#tuwei/views.py
#django模块导入
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
import hashlib,re
from django.http import Http404


from tuwei.models import WeixinUser
from WeiLib.lib import (WeiSession,GetMsg,TextMsg,check_signature)

try:
    from weixin2py.localsettings import TOKEN
except:
    from weixin2py.settings import TOKEN


       
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
        recv_msg = GetMsg(request.body)
        if recv_msg.msg_type == 'text': 
            msg = TextMsg(recv_msg.to_user_name, recv_msg.from_user_name, recv_msg.create_time)
            msg.make_msg("微信收到您的消息回复了\n测试换行")
            return render_to_response('response/msg_text.xml', 
                                      {'msg' : msg,}
                                      )
                

        elif recv_msg.msg_type == 'event':
            if recv_msg.event == u'subscribe':
                msg = TextMsg()
                msg_init(msg,recv_msg)
                msg.content = DEFAULT_MSG
                return render_to_response('response/text_to_user.xml',locals())
            else :
                return HttpResponse('成功取消关注！')