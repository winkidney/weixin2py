# coding:utf-8
from django.contrib import admin
from .models import (DBTextMsg, PatternT2T, DBImgTextMsg, PatternT2PT,
                     PatternE2PT, PatternE2T)


admin.site.register(PatternT2T)
admin.site.register(PatternT2PT)
admin.site.register(PatternE2PT)
admin.site.register(PatternE2T)
admin.site.register(DBTextMsg)
admin.site.register(DBImgTextMsg)
