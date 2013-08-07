#coding:utf-8
#in folder 'core'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InterestsTags(models.Model):
    tag_name = models.CharField(max_length=16,verbose_name=u'兴趣标签')
    def __unicode__(self):
		return u"%s %s" % (self.id,self.tag_name) 
class College(models.Model):
    college_name = models.CharField(max_length=20,verbose_name=u'学院')
    def __unicode__(self):
        return u"%s %s" % (self.id,self.college_name) 
class WeixinUserProfile(models.Model):
    '''存储用户详细信息的一个页面'''
    weixin_id = models.CharField(max_length=30,blank=True,verbose_name=u'微信号')
    student_id = models.CharField(max_length=11,blank=True,verbose_name=u'学号')
    student_pwd = models.CharField(max_length=20,blank=True,verbose_name=u'教务系统密码')
    interests_tags = models.ManyToManyField(InterestsTags,blank=True,verbose_name=u'兴趣标签')
    college_name = models.ManyToManyField(College,blank=True)
    student_name = models.CharField(max_length=10,blank=True,verbose_name=u'姓名')
    bbs_username = models.CharField(max_length=20,blank=True,verbose_name='彼岸帐号')
    bbs_pwd = models.CharField(max_length=20,blank=True,verbose_name=u'彼岸密码')
    def __unicode__(self):
        return u"%s %s" % (self.id,self.weixin_id) 
class WeixinUser(models.Model):
    '''微信用户openid的存储，简单的包括了用户菜单状态和勾搭是否开启的布尔值，
    因为经常更改所以设计为只包含这几项，使用一个一对一项将用户的详细信息包含到W WeixinUserProfile'''
    auth_user = models.OneToOneField(User,blank=True)#拓展用户
    nickname = models.CharField(max_length=30,blank=True,verbose_name=u'昵称')
    openid = models.CharField(max_length=40,verbose_name=u'微信OpenID')
    gouda_off = models.BooleanField(verbose_name=u'勾搭功能未打开')   #勾搭是否开启
    profile = models.OneToOneField(WeixinUserProfile,verbose_name=u'用户详细信息')
    is_bind = models.BooleanField(verbose_name=u'是否绑定学号')
    def __unicode__(self):
        return u"%s %s" % (self.id,self.openid) 
#拓展用户的一个函数，当不存在profile的时候则制造一个profile
def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = WeixinUser()
        profile.user = instance
        profile.save()
#拓展结束
