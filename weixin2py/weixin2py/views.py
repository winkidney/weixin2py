#coding:utf-8
#views of weixin2py foleder
#django模块导入
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.views.decorators.csrf import csrf_exempt
import hashlib,re
from django.http import Http404
#自定义模块导入
from core.msg_classes import TextMsg,ImgMsg,PicTextMsg
from tools.xml_reader import UserMsg
from tools import score_query
from core.views import create_new_user,user_exist
#数据库，全局变量
from core.models import WeixinUser
from core.session_class import WeiSession
from settings import SESSION_DICT

#测试结束
#全局变量
TOKEN = 'kidney'

DEFAULT_MSG =u'''
---------------------------------------------------
欢迎关注彼岸社区微信平台o(∩_∩)o 
你可以输入以下关键字进入相关功能
课表    成绩    二手    
借书    通知    新闻
勾搭    树洞    学霸    FAQ    
某些功能需要先绑定帐号哦！
输入“绑定”以绑定帐号～～
---------------------------------------------------
'''
BIND_MSG = u'''
---------------------------------------------------
欢迎关注彼岸社区微信平台o(∩_∩)o 
你可以输入以下关键字进入相关功能
课表    成绩    二手    
借书    通知    新闻
勾搭    树洞    学霸    FAQ    
获取帮助请发送“帮助”^_^
---------------------------------------------------
'''
#我的session_dict监控线程
import threading,time
def session_brusher(session_dict):
    while 1:
        time.sleep(20)
        deleted_list = []
        print 'the dict now is '+str(SESSION_DICT)
        if session_dict:
            for key in session_dict:
                if (datetime.datetime.now()-session_dict[key].lastcommit_time).seconds > 15*60:
                    deleted_list.append(key)
            for key in deleted_list:
                try:
                     del session_dict[key]
                except:
                    pass
        else:
            continue                                
import socket,sys
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    s.bind(('127.0.0.1',10086))
    brusher = threading.Thread(target=session_brusher,args=(SESSION_DICT,))
    brusher.setDaemon(True)
    brusher.start()
except:
    pass
#监控线程结束
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
        #为这个微信用户新增一个session状态
        if not SESSION_DICT.get(received_msg.from_user_name):
            SESSION_DICT[received_msg.from_user_name] = WeiSession()
        current_session = SESSION_DICT[received_msg.from_user_name]
        #在用户没有会话的情况下进行正常的文字消息处理
        if received_msg.msg_type == 'text': #处理文字类型的消息
                #如果用户输入“退出”，则将会话状态status置空，退回主菜单
            if received_msg.content == u'退出':
                SESSION_DICT[received_msg.from_user_name].status = u''
                #验证会话，如果用户有会话存在则直接调用会话处理，如果没有则进行主菜单消息处理
            if current_session.status:
                current_session.update()
                return FUNCTION_DICT[STATUS_DICT[current_session.status]](received_msg,1)   #传入一个标志’1‘来表示为子菜单状态
            #主菜单模式消息处理
            if received_msg.content in FUNCTION_DICT: #使用一个dict对象进行匹配以免进行大量的if else语法，导致代码很难看
                return FUNCTION_DICT[received_msg.content](received_msg)
            else:
                return default_response(received_msg)
            #收到事件推送的处理
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
def is_bind(received_msg):
    '''查询用户是否已经绑定学号密码'''
    user = WeixinUser.objects.get(openid=str(received_msg.from_user_name))
    if user.is_bind:
        return True
    else:
        return False
#默认回复
def default_response(received_msg):
    user = WeixinUser.objects.get(openid=str(received_msg.from_user_name))
    msg = TextMsg()
    msg_init(msg,received_msg)
    if user.is_bind:
        msg.content = BIND_MSG
    else:
        msg.content = DEFAULT_MSG
    return render_to_response('response/text_to_user.xml',locals())
#以下所有的函数对象都返回一个httpresponse对象，都使用received_msg作为输入参数，因为要使用
#openid作为会话对象

def get_score(received_msg):
    '''查询成绩,状态代码 r1'''
    msg = TextMsg()
    msg_init(msg,received_msg)
    user = WeixinUser.objects.get(openid=str(received_msg.from_user_name))
    if is_bind(received_msg):
        query_result = score_query.main(user.profile.student_id,user.porfile.student_pwd)
        if query_result == 0: #错误代码0,网络错误
            msg.content = u'查询失败，目测学校服务器抽风啦～～'
        elif query_result == 1: #错误代码2,用户名密码错误
            msg.content = u'查询失败，用户名密码错误'
        else:
            msg.content = query_result
        return render_to_response('response/text_to_user.xml',locals())
    else:
        return bind(received_msg)
def bind(received_msg,in_menu=0):
    '''绑定学号密码,状态代码r0'''
    msg = TextMsg()
    msg_init(msg,received_msg)
    if in_menu == 1:    #如果已经进入绑定状态
        user = WeixinUser.objects.get(openid=str(received_msg.from_user_name))
        s = received_msg.content
        if u'@' in s:
            s = s.split(u'@')
            length = len(s[0])
            if length == 9 or length == 10:
                user_name = s[0]
                passwd = s[1]
                query_result = score_query.main(user_name,passwd)
                if query_result == 0: #错误代码0,网络错误
                    msg.content = u'绑定验证失败，目测学校服务器抽风啦～～'
                elif query_result == 1: #错误代码2,用户名密码错误
                    msg.content = u'绑定失败，学号密码错误,请您重新输入学号密码进行绑定'
                else:
                    user.profile.student_id = user_name
                    user.porfile.student_pwd = passwd
                    user.is_bind = True
                    user.save()
                    SESSION_DICT[received_msg.from_user_name].status = u''
                    msg.content = u"绑定成功"+'您可以使用顶级菜单的所有功能了～～获取帮助请发送“帮助”'  
        else:
            msg.content = u'输入格式有误，请重新输入，格式为“学号@密码”，不要输入空格或者在密码中包含@哦^_^'
            #return render_to_response('response/text_to_user.xml',locals())
    else:   #未进入绑定状态，提示如何进行绑定
        msg.content = '您需要先绑定学号密码才能查询成绩～～请输入‘学号@密码’进行绑定。范例：031140848@123456\nK123456789@pwd,不要含有空格等字符哦,发送“退出”以退出成绩查询状态！'
        SESSION_DICT[received_msg.from_user_name].status = u'绑定'
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
def send_test():
    pass
STATUS_DICT = {u'绑定':u'绑定',
               }
FUNCTION_DICT = {u'成绩':get_score,u'绑定':bind,
                 }