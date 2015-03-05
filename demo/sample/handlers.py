# coding:utf-8

from weixin2py.utils import PTItem
from weixin2py.utils import text_response, pic_text_response


def test_handler(recv_msg, *args, **kwargs):
    title = "测试图文消息"
    description = "图文消息描述"
    pic_url = "//placeimg.com/160/100/any"
    url = "http://www.baidu.com"
    items = [PTItem(title, description, pic_url, url), ] * 2
    return pic_text_response(recv_msg, items)


def about_handler(recv_msg, *args, **kwargs):
    content = """
    关于我们
    """
    return text_response(recv_msg, content)


def subscribe_handler(recv_msg, *args, **kwargs):
    content = """
    --键入小写命令--
    """
    return text_response(recv_msg, content)


def help_handler(recv_msg, *args, **kwargs):
    return subscribe_handler(recv_msg, *args, **kwargs)
