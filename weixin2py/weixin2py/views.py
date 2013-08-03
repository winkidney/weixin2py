#coding:utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.http import Http404
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
        pass
        
    
    