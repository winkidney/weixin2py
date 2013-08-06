#coding:utf-8
#folder:weixin2py
#classes of all kind of response messages|所有发送的消息的类文件
class TextMsg(object):
    '''文字消息类'''
    def __init__(self):
        self.to_user_name = ''
        self.from_user_name = ''
        self.create_time = ''
        self.content = ''
class ImgMsg(object):
    '''图片消息类'''
    def __init__(self):
        self.to_user_name = ''
        self.from_user_name = ''
        self.create_time = ''
        self.title = ''
        self.description = ''
        self.music_url = ''
        self.hq_music_url = ''
class PicTextMsg(object):
    '''图文消息类'''
    def __init__(self):
        self.to_user_name = ''
        self.from_user_name = ''
        self.create_time = ''
        self.article_count = ''
        self.meassages = []
    def new_msg(self,title,description,pic_url,url):
        msg ={'title':title,
               'description':description,
               'pic_url':pic_url,
               'url':url,}
        self.messages.append(msg)
        del msg