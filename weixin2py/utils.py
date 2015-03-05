# coding:utf-8
import re
import urllib2
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import Context, Template
from django.core.cache import cache
from . import TextMsg, ImgMsg, PicTextMsg, PTItem

try:
    import cPickle as pickle
except ImportError:
    import pickle

from .plugin.setting import plugin_text as PLUGINS

DEFAULT_TIMEOUT = 15 * 60


class WeiSession(object):

    """ Helper Class to store info by session ID(Default: OpenID),
        Because of its usage of pickle, some type of data can't be stored correctly.
    """

    def __init__(self, session_id):
        if not isinstance(session_id, (str, unicode, int)):
            raise TypeError("Argument openid [%s] must be a str/unicode/int object!")
        self.session_id = session_id
        self._get_session()

    def _get_session(self):
        session = cache.get(self.session_id)
        if not session:
            self.session = {}
        else:
            self.session = pickle.loads(session)

    def _save(self):
        session_storage = pickle.dumps(self.session)
        cache.set(self.session_id, session_storage, DEFAULT_TIMEOUT)

    def set_key(self, key, value):
        self.session[key] = value
        self._save()

    def get_key(self, key):
        return self.session.get(key)


def create_menu(access_token, menu_list):
    """
    Create WeiChat menu in WeiChat Client.
    :param access_token: access_token str
    :param menu_list:
    :return:
    """
    url = """ https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s""" \
        % access_token
    data = render_to_string('send/menu_create.json', {'menu_list': menu_list})

    encoded_data = data.encode('utf-8')
    try:
        result = urllib2.urlopen(url, encoded_data, 20).read()
    except urllib2.URLError, urllib2.HTTPError:
        return False
    if result:
        if re.findall('ok', result):
            return True
    else:
        return False


def render_from_string(string, data):
    t = Template(string)
    return t.render(Context(data))


def text_response(recv_msg, content):
    msg = TextMsg(
        recv_msg.to_user_name, recv_msg.from_user_name, recv_msg.create_time)
    plugin_dict = {}
    for plugin in PLUGINS:
        result = plugin.processor(recv_msg)
        if isinstance(result, dict):
            plugin_dict.update(result)
    msg.make_msg(render_from_string(content, plugin_dict))
    return render_to_response('response/msg_text.xml',
                              {'msg': msg, }
                              )


def image_response(recv_msg, media_id):
    msg = ImgMsg(
        recv_msg.to_user_name, recv_msg.from_user_name, recv_msg.create_time)
    msg.make_msg(media_id)
    return render_to_response('response/msg_text.xml',
                              {'msg': msg, }
                              )


def pic_text_response(recv_msg, msg_item):
    msg = PicTextMsg(recv_msg.to_user_name, recv_msg.from_user_name, recv_msg.create_time)
    if isinstance(msg_item, PTItem):
        article_count = 1
        msg.new_item(
            msg_item.title, msg_item.description, msg_item.pic_url, msg_item.url)
    elif isinstance(msg_item, list):
        article_count = len(msg_item)
        for item in msg_item:
            msg.new_item(item.title, item.description, item.pic_url, item.url)
    else:
        raise ValueError("msg_item must be instance of list or PTItem.")
    msg.make_msg(article_count)
    return render_to_response('response/msg_pic_text.xml',
                              {'msg': msg, }
                              )
