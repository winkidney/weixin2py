#kill `cat blogfcgi.pid`
python manage.py runfcgi method=threaded host=127.0.0.1 port=8020 maxchildren=300 pidfile=/tmp/weixinfcgi.pid
