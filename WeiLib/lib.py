#coding:utf-8
# WeiLib/lib.py - contains libs of weichat message 
# and some tool function.
#read xml text and return a xml object
import datetime
import re,hashlib

#basic info
re_msg_type = re.compile(r"<MsgType><!\[CDATA\[(.*?)\]\]></MsgType>")
re_msg_tuid = re.compile(r"<ToUserName><!\[CDATA\[(.*?)\]\]></ToUserName>")
re_msg_fuid = re.compile(r"<FromUserName><!\[CDATA\[(.*?)\]\]></FromUserName>")
re_msg_ctime = re.compile(r"<CreateTime>(.*?)</CreateTime>")
re_msg_id = re.compile(r"<MsgId>(.*?)</MsgId>")
re_media_id = re.compile(r"<MediaId><!\[CDATA\[(.*?)\]\]></MediaId>")
#text msg
re_text_content = re.compile(r"<Content><!\[CDATA\[(.*?)\]\]></Content>")


#img msg
re_img_url = re.compile(r"<PicUrl><!\[CDATA\[(.*?)\]\]></PicUrl>")
re_img_id = re.compile(r"")
#location msg
re_locx = re.compile(r"<Location_X>(.*?)</Location_X>")
re_locy = re.compile(r"<Location_Y>(.*?)</Location_Y>")
re_scale = re.compile(r"<Scale>(.*?)</Scale>")
re_label = re.compile(r"<Label><!\[CDATA\[(.*?)\]\]></Label>")

#link msg
re_title = re.compile(r"<Title><!\[CDATA\[(.*?)\]\]></Title>")
re_description = re.compile(r"<Description><!\[CDATA\[(.*?)\]\]></Description>")
re_url = re.compile(r"<Url><!\[CDATA\[(.*?)\]\]></Url>")

#event msg
re_event = re.compile(r"<Event><!\[CDATA\[(.*?)\]\]></Event>")
re_eventkey = re.compile(r"<EventKey><!\[CDATA\[(.*?)\]\]></EventKey>")

class GetMsg(object):
    '''输入一个xml文本字符串对象，生成一个object并返回'''
    def get_info(self, regx, msg):
        result = re.findall(regx, msg)
        if result:
            return result[0]
       
    def get_text_msg(self, msg):
        '''文本消息'''

        self.content = self.get_info(re_text_content, msg)
        
    def get_img_msg(self, msg):
        '''图片消息'''

        self.pic_url =  self.get_info(re_img_url, msg)
        self.media_id = self.ge_info(re_media_id, msg)
        
    def get_location_msg(self, msg):
        '''地理位置消息'''

        self.location_x =  self.get_info(re_locx, msg)
        self.location_y =  self.get_info(re_locy, msg)
        self.scale =  self.get_info(re_scale, msg)
        self.label =  self.get_info(re_label, msg)

        
    def get_link_msg(self, msg):
        
        '''链接消息推送'''
        
        self.title =  self.get_info(re_title, msg)
        self.description =  self.get_info(re_description, msg)
        self.url =  self.get_info(re_url, msg)

        
    def get_event_msg(self, msg):
        '''事件推送'''
        self.event =  self.get_info(re_event, msg)
        self.event_key =  self.get_info(re_eventkey, msg)
        
    def __init__(self, msg):
        '''传入一个xml字符串来初始化类，自动生成一个文档树，
        并调用get_object函数获得一个包含消息各个属性的对象'''
        self.to_user_name = self.get_info(re_msg_tuid, msg)
        self.from_user_name = self.get_info(re_msg_fuid, msg)
        self.create_time = self.get_info(re_msg_ctime, msg)
        self.msg_type = self.get_info(re_msg_type, msg)
        self.msg_id = self.get_info(re_msg_id, msg)
        msgtype = self.msg_type
        if msgtype == 'text':
            self.get_text_msg( msg )
        elif msgtype == 'image':
            self.get_img_msg( msg )
        elif msgtype == 'location':
            self.get_location_msg( msg )
        elif msgtype == 'link':
            self.get_link_msg( msg )
        elif msgtype == 'event':
            self.get_event_msg( msg )
            

class WeiSession(object):
    '''微信助手会话类，用来存储用户的会话状态'''
    def __init__(self):
        self.get_status()
        self.status = u''
    
    def get_status(self,):
        pass
    
    def save(self):
        pass
    
    def update(self):
        pass
    
    def menu_out(self,):
        self.status = self.status[0:-2]
    
    def menu_in(self,menu_obj):
        self.status = self.status+menu_obj
    
    def exit(self):
        self.status =''
        
# Message for response to user
class ResMsg(object):
    
    """Message response to user."""
    
    to_user_name = ''
    from_user_name = ''
    create_time = ''
    function_flag = ''
    
    def __init__(self, to_user, from_user, ctime, func_flag=0):
        self.to_user_name = from_user
        self.from_user_name = to_user
        self.create_time = int(ctime)+1
        self.function_flag = func_flag
        
class TextMsg(ResMsg):
    
    '''文字消息类'''
    
    def make_msg(self, content):
        self.content = content
        
class MusicMsg(ResMsg):
    
    '''music message'''
    
    def make_msg(self, title, description, music_url, hq, media_id=0):
        self.title = title
        self.description = description
        self.music_url = music_url
        self.hq_music_url = hq
        self.media_id = media_id
class ImgMsg(ResMsg):
    
    """Image message"""
    
    def make_msg(self, media_id):
        self.media_id = media_id
        
class PicTextMsg(ResMsg):
    
    '''图文消息类'''
    
    def make_msg(self, article_count):
        
        self.article_count = ''
        self.articles = []
        
    def new_item(self, title, description, pic_url, url):
        item ={'title' : title,
              'description' : description,
              'pic_url' : pic_url,
              'url': url,}
        self.articles.append(item)


def check_signature(request, TOKEN):
    '''检查消息是否是微信发过来的'''
    request_dict = request.GET
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