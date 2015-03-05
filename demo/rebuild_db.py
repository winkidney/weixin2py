#!/usr/bin/env python
# coding:utf-8

import sys
import os
from django.core import management
import django


sys.path.append(os.path.realpath(__file__).replace('\\', '/'))


if os.path.isfile("wei_demo/localsettings.py"):
    os.environ['DJANGO_SETTINGS_MODULE'] = "wei_demo.localsettings"
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = "wei_demo.settings"


from django.contrib.auth.models import User

django.setup()


def syncdb_with_su(su_name, su_email, su_passwd):
    # sync db
    management.call_command('syncdb', interactive=False)
    print "sync done"
    # create super user
    user = User.objects.create_superuser(su_name, su_email, su_passwd)
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.save()
    print "super user added"

if __name__ == '__main__':
    if os.path.isfile('weixin2py.db'):
        os.remove('weixin2py.db')
    syncdb_with_su('admin', 'admin@admin.com', 'admin')
