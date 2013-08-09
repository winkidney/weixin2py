#coding:utf-8
#views of weixin2py foleder
#django模块导入
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.http import Http404
#自定义模块导入
from msg_classes import TextMsg,ImgMsg,PicTextMsg
from tools.xml_reader import UserMsg
from tools import score_query
from core.views import create_new_user,user_exist
#数据库，全局变量
from core.session_class import WeiSession
from settings import SESSION_DICT

#测试结束
#全局变量
TOKEN = 'kidney'

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
        if not user_exist(received_msg):    #检测当前微信用户是否存在，如果不存在则创建一个新的用户，用户对应的django账户为微信openid，密码为openid
            create_new_user(received_msg)   #创建一个新用户
        if received_msg.msg_type == 'text': #处理文字类型的消息
            if received_msg.content in FUNCTION_DICT: #使用一个dict对象进行匹配以免进行大量的if else语法，导致代码很难看
                return FUNCTION_DICT[received_msg.content](received_msg)
            else:
                return defult_response(received_msg)
        elif received_msg.msg_type == 'event':
            if received_msg.event == u'subscribe':
                msg = TextMsg()
                msg_init(msg,received_msg)
                msg.content = DEFAULT_MSG
                return render_to_response('response/text_to_user.xml',locals())
            else :
                return HttpResponse('成功取消关注！')
#一些公用的消息初始化,要在每一个消息生成之前调用这个函数，不然会出错 
def msg_init(msg,received_msg):
    msg.from_user_name = received_msg.to_user_name
    msg.to_user_name = received_msg.from_user_name
    msg.create_time = str(int(received_msg.create_time)+1)
    return
#默认回复
def default_response(recived_msg):
    msg = TextMsg()
    msg_init(msg,received_msg)
    msg.content = DEFAULT_MSG
    return render_to_response('response/text_to_user.xml',locals())
#以下所有的函数对象都返回一个httpresponse对象，都使用received_msg作为输入参数，因为要使用
#openid作为会话对象
def get_score(received_msg):
    '''查询成绩'''
    msg = TextMsg()
    msg_init(msg,received_msg)
    query_result = score_query.main('031140816','19921226')
    if query_result == 0: #错误代码0,网络错误
        msg.content = u'查询失败，目测学校服务器抽风啦～～'
    elif query_result == 1: #错误代码2,用户名密码错误
        msg.content = u'查询失败，用户名密码错误'
    else:
        msg.content = query_result
    return render_to_response('response/text_to_user.xml',locals())
def get_class_table():
    '''查询课表'''
    pass    
def second_hand():
    '''二手查询'''
    pass
def books_query():
    '''图书馆借书查询'''
    pass
def get_notification():
    '''通知'''
    pass
def get_news():
    '''新闻'''
    pass
def gou_da():
    '''勾搭功能'''
def tu_cao():
    '''吐槽'''
    pass
def help():
    '''帮助系统'''
    pass
FUNCTION_DICT = {u'成绩':get_score,
                 }