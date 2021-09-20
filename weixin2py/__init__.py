# coding:utf-8
import hashlib
import os
import re
import urllib2


def weixin2py_template_dir():
    return os.path.abspath(
        os.path.dirname(__file__)).replace('\\', '/')


# basic info
re_msg_type = re.compile(r"<MsgType><!\[CDATA\[(.*?)\]\]></MsgType>")
re_msg_tuid = re.compile(r"<ToUserName><!\[CDATA\[(.*?)\]\]></ToUserName>")
re_msg_fuid = re.compile(r"<FromUserName><!\[CDATA\[(.*?)\]\]></FromUserName>")
re_msg_ctime = re.compile(r"<CreateTime>(.*?)</CreateTime>")
re_msg_id = re.compile(r"<MsgId>(.*?)</MsgId>")
re_media_id = re.compile(r"<MediaId><!\[CDATA\[(.*?)\]\]></MediaId>")
# text msg
re_text_content = re.compile(r"<Content><!\[CDATA\[(.*?)\]\]></Content>")


# img msg
re_img_url = re.compile(r"<PicUrl><!\[CDATA\[(.*?)\]\]></PicUrl>")
re_img_id = re.compile(r"")
# location msg
re_locx = re.compile(r"<Location_X>(.*?)</Location_X>")
re_locy = re.compile(r"<Location_Y>(.*?)</Location_Y>")
re_scale = re.compile(r"<Scale>(.*?)</Scale>")
re_label = re.compile(r"<Label><!\[CDATA\[(.*?)\]\]></Label>")

# link msg
re_title = re.compile(r"<Title><!\[CDATA\[(.*?)\]\]></Title>")
re_description = re.compile(r"<Description><!\[CDATA\[(.*?)\]\]></Description>")
re_url = re.compile(r"<Url><!\[CDATA\[(.*?)\]\]></Url>")

# event msg
re_event = re.compile(r"<Event><!\[CDATA\[(.*?)\]\]></Event>")
re_eventkey = re.compile(r"<EventKey><!\[CDATA\[(.*?)\]\]></EventKey>")


class WeiMsg(object):

    """输入一个xml文本字符串对象，生成一个object并返回"""

    def get_info(self, regx, msg):
        result = re.findall(regx, msg)
        if result:
            return result[0]
        else:
            return ''

    def get_text_msg(self, msg):

        self.content = self.get_info(re_text_content, msg)

    def get_img_msg(self, msg):
        """图片消息"""

        self.pic_url = self.get_info(re_img_url, msg)
        self.media_id = self.get_info(re_media_id, msg)

    def get_location_msg(self, msg):
        """地理位置消息"""

        self.location_x = self.get_info(re_locx, msg)
        self.location_y = self.get_info(re_locy, msg)
        self.scale = self.get_info(re_scale, msg)
        self.label = self.get_info(re_label, msg)

    def get_link_msg(self, msg):
        """链接消息推送"""

        self.title = self.get_info(re_title, msg)
        self.description = self.get_info(re_description, msg)
        self.url = self.get_info(re_url, msg)

    def get_event_msg(self, msg):
        """事件推送"""
        self.event = self.get_info(re_event, msg)
        self.event_key = self.get_info(re_eventkey, msg)

    def __init__(self, msg):
        """generate a message object
        """
        self.to_user_name = self.get_info(re_msg_tuid, msg)
        self.from_user_name = self.get_info(re_msg_fuid, msg)
        self.create_time = self.get_info(re_msg_ctime, msg)
        self.msg_type = self.get_info(re_msg_type, msg)
        self.msg_id = self.get_info(re_msg_id, msg)
        msgtype = self.msg_type
        if msgtype == 'text':
            self.get_text_msg(msg)
        elif msgtype == 'image':
            self.get_img_msg(msg)
        elif msgtype == 'location':
            self.get_location_msg(msg)
        elif msgtype == 'link':
            self.get_link_msg(msg)
        elif msgtype == 'event':
            self.get_event_msg(msg)



# Message for response to user
class BaseReMsg(object):

    """Base returned message for client."""

    def __init__(self, to_user, from_user, ctime, func_flag=0):
        """
        Normal init by (to_user, from_user, ctime, func_flag).
        :param to_user: target openid
        :type to_user: str, unicode, int
        :param from_user: openid
        :type from_user: str, unicode, int
        :param ctime: the origin msg send time(unix timestamp).
        :param func_flag: weichat func_flag.
        :return:
        """
        self.to_user_name = from_user
        self.from_user_name = to_user
        self.create_time = int(ctime) + 1
        self.function_flag = func_flag


class TextMsg(BaseReMsg):

    """文字消息类"""

    def make_msg(self, content):
        self.content = content


class MusicMsg(BaseReMsg):

    """music message"""

    def make_msg(self, title, description, music_url, hq, media_id=0):
        self.title = title
        self.description = description
        self.music_url = music_url
        self.hq_music_url = hq
        self.media_id = media_id


class ImgMsg(BaseReMsg):

    """Image message"""

    def make_msg(self, media_id):
        self.media_id = media_id


class PicTextMsg(BaseReMsg):

    """图文消息类"""

    def __init__(self, to_user, from_user, ctime, func_flag=0):
        super(PicTextMsg, self).__init__(
            to_user, from_user, ctime, func_flag=0)
        self.articles = []

    def make_msg(self, article_count):

        self.article_count = article_count

    def new_item(self, title, description, pic_url, url):
        item = {'title': title,
                'description': description,
                'pic_url': pic_url,
                'url': url, }
        self.articles.append(item)


class PTItem(object):

    def __init__(self, title, description, pic_url, url):
        self.title = title
        self.description = description
        self.pic_url = pic_url
        self.url = url


class MButton(object):

    """ button class of the weichat meun"""

    def __init__(self, name, **kwargs):
        self.type = None
        self.key = None
        self.url = None
        self.sub_buttons = []
        self.name = name
        url = kwargs.get('url')
        key = kwargs.get('key')
        if url or key:
            if url:
                self.make_view(url)
            else:
                self.make_click(key)

    def make_click(self, key):
        self.type = 'click'
        self.key = key

    def make_view(self, url):
        self.type = 'view'
        self.url = url

    def add_button(self, button):
        if isinstance(button, MButton):
            self.sub_buttons.append(button)
        else:
            raise TypeError


def check_signature(request, token):
    """Verify if the author of received msg is tencent."""
    request_dict = request.GET
    if request_dict.get('signature') and request_dict.get('timestamp') \
            and request_dict.get('nonce') and request_dict.get('echostr'):
        signature = request_dict.get('signature')
        timestamp = request_dict.get('timestamp')
        nonce = request_dict.get('nonce')
        token = token
        tmplist = sorted([token, timestamp, nonce])
        newstr = ''.join(tmplist)
        sha1result = hashlib.sha1()
        sha1result.update(newstr)
        if sha1result.hexdigest() == str(signature):
            return True
        else:
            return False
    else:
        return False


def get_atoken(app_id, app_secret):
    """
    Get AccessToken by appid and appsecret.
    :param app_id:
    :param app_secret: Tencent appsecret
    :return: Access token.
    :rtype str or unicode
    """
    url = """https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%(appid)s&secret=%(appsecret)s""" \
        % {'appid': app_id, 'appsecret': app_secret}

    try:
        result = urllib2.urlopen(url, timeout=20).read()
    except urllib2.HTTPError, urllib2.URLError:
        return None
    if result:
        if re.findall('"access_token":"(.*?)"', result):
            return result[0]
    return None


