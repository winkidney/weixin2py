#coding:utf-8
import MySQLdb
import sys,os
from datetime import *
#设置系统环境以便在登记昂哦shell外部引用models功能
sys.path.append(os.path.join(os.path.dirname(__file__),'').replace('\\','/'),)
os.environ['DJANGO_SETTINGS_MODULE'] ='weixin2py.settings'
from django.core.management import setup_environ
from weixin2py import settings
from core.models import *
setup_environ(settings)
#系统环境设置完毕

dbname = 'weixin2py'
rootusername = 'root'
root_passwd = '19921226'
tables_to_delete = 'core_college,core_intereststags,core_weixinuser,core_weixinuserprofile,core_weixinuserprofile_college_name,core_weixinuserprofile_interests_tags;'#
#try:
#	sys.argv[1] and sys.argv[2]
#except :
#	print "use create_db.py "
#	sys.exit()
#db_name = str(sys.argv[1])
#passwd = str(sys.argv[2])

try:
	conn=MySQLdb.Connect(host='localhost',user=rootusername,passwd=root_passwd)
	cursor =conn.cursor()
	cursor.execute('use %s' % dbname)
	cursor.execute('drop table %s' % tables_to_delete)  #CREATE USER user01@'localhost' IDENTIFIED BY 'password1';
	#conn.commit() 
except Exception, e:
    print 'modified database failed,errors below may help you'
    print e 
finally:
	print 'clear done,start syncdb'
	os.system('python manage.py syncdb')
	print "syncdb done"
	print "start init db"
	print 'done'
