#coding:utf-8
#in folder 'core'
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import WeixinUser,WeixinUserProfile,College,InterestsTags
from django.contrib.auth.models import User
#拓展用户
class ProfileInline(admin.StackedInline):
    model =  WeixinUser
    #fk_name = 'user'
    max_num = 1
    can_delete = False
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline,]
admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
#拓展用户结束
admin.site.register(WeixinUserProfile)
admin.site.register(College)
admin.site.register(InterestsTags)
