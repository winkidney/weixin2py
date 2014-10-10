# coding:utf-8
# tuwei/views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from weilib.router import base_router, db_router
from .router import router_patterns
from weilib.lib import GetMsg, check_signature
from weilib.handlers import default_handler

try:
    from wei_demo.localsettings import TOKEN
except ImportError:
    from wei_demo.settings import TOKEN

# router 必须是一个list实例
routers = [base_router, db_router]


@csrf_exempt
def home(request):
    if request.method == 'GET':
        response = HttpResponse()
        if check_signature(request, TOKEN):
            response.write(request.GET.get('echostr'))
            return response
        else:
            response.write('不提供直接访问！')
            return response

    if request.method == 'POST':
        #check_signature(request, TOKEN)
        recv_msg = GetMsg(request.body)
        for router in routers:
            result = router(recv_msg, router_patterns)
            if isinstance(result, HttpResponse):
                return result
        return default_handler(recv_msg)
