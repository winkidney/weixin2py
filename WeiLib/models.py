#coding:utf-8
#WeiLib/models.py - database definition file of WeiLib
#by kidney 2014.05.12
from django.db import models

MSG_TYPES = (
    ('text', '文本消息'),
    ('event', '时间消息'),
    ('image', '图片消息'),
    ('location', '位置消息'),
    ('voice', '语音消息'),
    ('video', '视频消息'),
)
EVENTS =(
         ('subscribe','关注事件'),
         ('unsubscribe','取消关注事件'),
         ('SCAN','扫描二维码'),
         ('LOCATION', '上报地理位置'),
         ('CLICK', '自定义菜单事件'),
         ('VIEW', '用户点击链接跳转时候的事件'),
         )

class DBTextMsg(models.Model):
    
    """msg in database"""
    class Meta:
        verbose_name = 'Z文字消息管理'
        verbose_name_plural = 'Z文字回复消息管理'
    content = models.TextField(blank=False,verbose_name="内容")


class DBImgTextMsg(models.Model):
    
    """image_text msg in database"""
    class Meta:
        verbose_name = 'Z图文消息管理'
        verbose_name_plural = 'Z图文消息管理'
        
    title = models.CharField(blank=True, max_length=255, verbose_name="标题")
    description = models.CharField(blank=True, max_length=255, verbose_name="描述")
    pic_url = models.URLField(blank=False, verbose_name="图片地址")
    url = models.URLField(blank=False, max_length=255, verbose_name="文章地址")

class PatternE2T(models.Model):
    
    """text response pattern to user"""
    class Meta:
        verbose_name = 'M事件>文本消息回复规则'
        verbose_name_plural = 'M事件>文本消息回复规则'

    type = models.CharField(max_length=20,
                            choices=MSG_TYPES,
                            default='event',verbose_name="消息类型")
    event = models.CharField(max_length=30,
                             choices=EVENTS,
                             default='CLICK',verbose_name="事件类型")
    event_key = models.CharField(blank=True, max_length=50,help_text='对于自定义菜单事件这个是必填的！')
    handler = models.ForeignKey(DBTextMsg, verbose_name="回复消息")

class PatternE2PT(models.Model):
    
    """text response pattern to user"""
    class Meta:
        verbose_name = 'M事件>图文消息回复规则'
        verbose_name_plural = 'M事件>图文消息回复规则'

    type = models.CharField(max_length=20,
                            choices=MSG_TYPES,
                            default='event',verbose_name="消息类型",
                            help_text="除非你清楚这个字段的含义，否则请不要随意更改")
    event = models.CharField(max_length=30,
                             choices=EVENTS,
                             default='CLICK',verbose_name="事件类型")
    event_key = models.CharField(blank=False, max_length=50)
    handler = models.ManyToManyField(DBImgTextMsg, verbose_name="回复消息", help_text="最多允许五条，不然会出错")

class PatternT2PT(models.Model):
    
    """image_text response pattern to user"""
    class Meta:
        verbose_name = 'M文本>图文消息回复规则'
        verbose_name_plural = 'M文本>图文消息回复规则'
    type = models.CharField(max_length=20,
                            choices=MSG_TYPES,
                            default='text',
                            help_text="除非你清楚这个字段的含义，否则请不要随意更改")
    cotent = models.CharField(max_length=50, blank=True)
    handler = models.ManyToManyField(DBImgTextMsg, verbose_name="回复消息", help_text="最多允许五条，不然会出错")

class PatternT2T(models.Model):
    
    """text response pattern to user"""
    class Meta:
        verbose_name = 'M文本>文本消息回复规则'
        verbose_name_plural = 'M文本>文本消息回复规则'
        
    type = models.CharField(max_length=20,
                            choices=MSG_TYPES,
                            default='text',
                            help_text="除非你清楚这个字段的含义，否则请不要随意更改")
    content = models.CharField(max_length=100, blank=True,verbose_name="收到的消息",
                               help_text="支持正则表达式")
    handler = models.ForeignKey(DBTextMsg, verbose_name="响应的消息内容")









