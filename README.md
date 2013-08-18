#weixin2py--微信公众平台接口程序

### 1.简介

* 使用python2.7和django 1.5.1开发的微信公众平台服务端程序，可以自动回复用户发来微信的消息。
* 最初的启发来自“武大助手”，类似的平台，提供校园信息服务&服务微信化
* 有什么 意见或者建议请发issue

### 2. 特性
* 当用户发来第一条消息的时候，自动检测用户是否存在并生成一个唯一的用户（使用openid），存储到数据库。
* 将从腾讯微信服务器接收到的消息转化为对象并可以让处理视图使用。
* 实现了自动回复用户消息，您可以自定义您的消息回复函数，构建一个新的django视图以完成处理。（例如，当用户输入“天气”，您可以定义一个消息匹配和获取天气的函数，給用户返回一个天气消息）
* 用户当前菜单功能状态存储（使用简单的session数组），例如，用户进入“绑定”功能，内存中的session字典将记录用户进入了绑定功能，并将接下来用户输入的信息交给绑定验证函数进行处理，而不是一级菜单的处理函数处理。由于功能较为简单，并未使用数据库存储，您可以根据自己的需要更改这个方式。
* 少许额外功能，例如绑定，还有适合本学校的成绩查询脚本。
* 消息模版，存储在weixin2py/templates下，方便使用render_to_response进行处理。

### 3. 安装，修改，使用
1. 本程序基于python2.7 django1.5.1开发，不保证在之前的版本能正常运行，但是理论上兼容py26和django1.4

2. 使用本程序之前必须先安装python2.7,django 1.5.1,您可以通过任何方式安装着两个程序

3. 将程序复制到你想要的文件夹，如果您是mysql数据库，修改create_db.py内的数据库配置，可以使用这个脚本创建所需数据库。
```python
rootusername = 'root'
root_passwd = 'db_root_pwd'
```
>如果您是彼得数据库，您必须手动创建这个数据库。
然后，修改您的settings.py
```python
if 'SERVER_SOFTWARE' in os.environ:
    from bae.core import const
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'you_apply_database_name',
            'USER': const.MYSQL_USER,
            'PASSWORD': const.MYSQL_PASS,  
            'HOST': const.MYSQL_HOST,  
            'PORT': const.MYSQL_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'weixin2py',
            'USER': 'weixin2py',
            'PASSWORD': 'yourpwd',    
            'HOST': 'localhost',                  
            'PORT': '3306',                      
        }
    }
```
将name修改为您的数据库名称，user修改为您的数据库用户，password设置为您的数据库用户。
您也可以选择别的数据库后端
接下来，运行python manage.py syncdb core初始化数据库，按照提示操作即可。
最后，修改您的settings.py中的TOKEN，改为您的公众帐号token即可。
此时，运行python manage.py 0.0.0.0:80即可运行测试服务器，如果您在您的威信公众帐号中已经设定好了url与token，那么您现在就可以开始使用本服务器了。



### 4. 关于
您可以自由使用代码，但是您必须注明出处和作者。

 [博客](http://blog.sina.com/winkidney) 

 [My-github](http://github.com/winkidney)

by winkidney 20130818


