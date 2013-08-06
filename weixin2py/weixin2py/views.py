#coding:utf-8
#views of weixin2py foleder
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.http import Http404
from msg_classes import TextMsg,ImgMsg,PicTextMsg
from tools.xml_reader import UserMsg
#全局变量
TOKEN = 'kidney'

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
        myresponse = HttpResponse()
        if check_signature(request.GET):
            myresponse.write(request.GET.get('echostr'))
            return myresponse
        else:
            myresponse.write('Fail!')
            return myresponse
    if request.method == 'POST':
        recived_msg = UserMsg(request.body)
        msg = TextMsg()
        #一些公用的消息处理
        msg.from_user_name = recived_msg.to_user_name
        msg.to_user_name = recived_msg.from_user_name
        msg.create_time = str(int(recived_msg.create_time)+1)
        if recived_msg.msg_type == 'text':
            text_response(msg,"欢迎使用湖北民族学院小助手，功能开发测试中～～")
            return render_to_response('response/text_to_user.xml',locals())
    
def text_response(msg,text):
    msg.content = text
    return