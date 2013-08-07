#coding:utf-8
#views of weixin2py foleder
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.http import Http404
from msg_classes import TextMsg,ImgMsg,PicTextMsg
from tools.xml_reader import UserMsg
#测试
from core.views import create_new_user
from tools import score_query
#测试结束
#全局变量
TOKEN = 'kidney'
SESSION_DICT = {}
DEFAULT_MSG =U'''
---------------------------------------------------
欢迎关注彼岸社区微信平台o(∩_∩)o 
你可以输入以下关键字进入相关功能
课表    成绩    二手    
借书    通知    新闻
勾搭    树洞    学霸    FAQ    
使用功能：请先绑定帐号哦！（url）
---------------------------------------------------
'''
def check_signature(request_dict):
    '''检查消息是否是微信发过来的'''
    if request_dict.get('signature') and request_dict.get('timestamp') and request_dict.get('nonce') and request_dict.get('echostr'):
        signature = request_dict.get('signature')
        timestamp = request_dict.get('timestamp')
        nonce = request_dict.get('nonce')
        token = TOKEN
        tmplist = [token,timestamp,nonce]
        tmplist.sort()
        newstr = ''.join(tmplist)
        sha1result = hashlib.sha1()
        sha1result.update(newstr)
        if sha1result.hexdigest() == str(signature):
            return True
        else:
            return False
    else:
        return False      
@csrf_exempt  
def home(request):
    if request.method == 'GET':
        #get方法的时候返回验证字符串
        myresponse = HttpResponse()
        if check_signature(request.GET):
            myresponse.write(request.GET.get('echostr'))
            return myresponse
        else:
            myresponse.write('不提供直接访问！')
            return myresponse
        #处理微信发过来的post请求
    if request.method == 'POST':
        received_msg = UserMsg(request.body)
        if received_msg.msg_type == 'text':
            if received_msg.content == u'成绩':
                msg = TextMsg()
                msg_init(msg,received_msg)
                query_result = score_query.main('031140816','19921226')
                if query_result:
                    msg.content = query_result
                else:
                    msg.content = u'查询失败，目测学校服务器抽风啦～～'
                return render_to_response('response/text_to_user.xml',locals())
            else:
                msg = TextMsg()
                msg_init(msg,received_msg)
                msg.content = DEFAULT_MSG
                return render_to_response('response/text_to_user.xml',locals())
        elif received_msg.msg_type == 'event':
            if received_msg.event == u'subscribe':
                msg = TextMsg()
                msg_init(msg,received_msg)
                msg.content = DEFAULT_MSG
                return render_to_response('response/text_to_user.xml',locals())
            else :
                return HttpResponse('成功取消关注！')
#一些公用的消息初始化    
def msg_init(msg,received_msg):
    msg.from_user_name = received_msg.to_user_name
    msg.to_user_name = received_msg.from_user_name
    msg.create_time = str(int(received_msg.create_time)+1)
    return
def get_score():
    pass
    
    
    
FUNCTION_DICT = {u'成绩':get_score
                 }