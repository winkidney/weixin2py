#---------------
#!/bin/sh

if [ $# != 1 ]
then 
    echo 'Usage: ctrl.sh start|stop|restart '
elif [ $1 = "start" ]
then
    python manage.py runfcgi method=threaded host=127.0.0.1 port=8020 maxchildren=300 pidfile=/tmp/weixinfcgi.pid
elif [ $1 = "stop" ] 
then 
    kill `cat /tmp/weixinfcgi.pid`
    echo 'weixin2py killed'
elif [ $1 = "restart" ]
then 
    kill `cat /tmp/weixinfcgi.pid`
    echo 'weixin2py killed\n'
    python manage.py runfcgi method=threaded host=127.0.0.1 port=8020 maxchildren=300 pidfile=/tmp/weixinfcgi.pid
    echo 'process started!'
fi
