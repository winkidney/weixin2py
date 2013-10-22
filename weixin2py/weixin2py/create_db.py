#coding:utf-8
import MySQLdb
try:
	from localsettings import *
except:
	dbname = ''
	rootusername = ''
	root_passwd = ''
	dbusername = ''
	password = ''



try:
	conn=MySQLdb.Connect(host='localhost',user=rootusername,passwd=root_passwd)
	cursor =conn.cursor()
	cursor.execute('create database %s;' % (dbname))
	cursor.execute("GRANT ALL PRIVILEGES ON `%s`.* TO '%s'@'localhost' IDENTIFIED BY '%s' WITH GRANT OPTION;" % (dbname,dbusername,password))  #CREATE USER user01@'localhost' IDENTIFIED BY 'password1';
	cursor.execute('FLUSH PRIVILEGES;')
except:
	print 'fail'
