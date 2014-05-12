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

class DBTextMsg(models.Model):
    
    """msg in database"""
    
    content = models.TextField(blank=False,verbose_name="内容")

class PatternT(models.Model):
    
    """text response pattern to user"""
   
    type = models.charField(max_length=20,
                            choices=MSG_TYPES,
                            default='text')
    event_key = models.CharField(max_length=50, blank=True)
    handler = models.ForeignKey(DBTextMsg)

class DBImgTextMsg(models.Model):
    
    """image_text msg in database"""
    title = models.CharField(blank=True, max_length=255, verbose_name="标题")
    description = models.charField(blank=True, max_length=255, verbose_name="描述")
    pic_url = models.URLField(blank=False, verbose_name="图片地址")
    url = models.URLField(blank=False, max_length=255, verbose_name="文章地址")

class PatternPT(models.Model):
    
    """image_text response pattern to user"""
    
    type = models.charField(max_length=20,
                            choices=MSG_TYPES,
                            default='text')
    event_key = models.CharField(max_length=50, blank=True)
    handler = models.ManyToManyField(DBImgTextMsg)











