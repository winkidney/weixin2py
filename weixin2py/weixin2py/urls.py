from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weixin2py.views.home', name='home'),
    # url(r'^weixin2py/', include('weixin2py.foo.urls')),
    url(r'^weichat/',include("tuwei.urls")),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
