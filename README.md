#weixin2py--微信公众平台web服务器

### 1.Summary

* 使用python2.7和django 1.5.1开发的微信公众平台服务端程序，可以自动回复用户发来微信的消息。
* 最初的启发来自“武大助手”，类似的平台，提供校园信息服务&服务微信化
* 有什么 意见或者建议请发issue

### 2. Feature
* 当用户发来第一条消息的时候，自动检测用户是否存在并生成一个唯一的用户（使用openid），存储到数据库。(新版本中尚未实现)
* 可拔插设计，提供django app ‘WeiLib’，里面有大部分可能用到的工具类和工具函数，需要的时候，新建你的django app，并且在app中使用WeiLib即可。
* 消息模版,WeiLil.llib中包含了text_response和pic_text_response函数，传入参数可以在任意view或者handler中使用.
* 示例应用中将实现一个简单的缓存session功能。更改你的缓存后端或者更改缓存接口即可。
* 新增路由功能((数据库路由和文件路由)，使用正则表达式对回复进行匹配，支持自定义规则。
* 插件支持，以便你可以在数据里定义非写死的回复消息。

目前新版本开发中，不保证任何可用性，需要老版（代码很丑陋）请移步：[这里](https://github.com/winkidney/weixin2py/tree/release1.0) 
### 3.How To
1. INSTALL
依赖于django1.5和python2.7，请先安装对应版本的django和python，不支持3.x。你可以使用如下方式安装python依赖：
```bash
apt-get install python-pip
pip install django>=1.5
```
接下来,打开你的bash，切换到应用根目录,执行
```bash
python rebuild.py
```
将会自动生成数据库并添加超级用户，用户名admin,密码admin，你可以自行去这个脚本修改。
```bash
sh runserver.sh
```
运行测试服务器（默认工作在80端口）。    
也可以使用nginx+*cgi,任何你喜欢的方式。    
2.  Basic Usage
访问http://youhost/admin/    
登录，添加消息回复规则即可。    
例如 想对用户发来的文本消息进行匹配，并回复一条文本消息，在管理面板中选择“文本>文本消息回复规则”，根据各个字段的提示进行填写即可。

### 4.Change Log
* 2014.05.09 - 2014.05.15 增加路由功能，插件功能。
* 2014.05.08 - 全面重构中
* 2013.xx.xx - first release,多么幼稚的代码

### 5.To Do List
1. 简化程序，并将通用处理过程提取出来，让处理函数可以直接方便的处理消息(done)
2. 将用户session改到key-value数据库存储或者内存缓存，提高效率和可靠性。(todo)
3. 修改数据库设定，让数据库具有通用性并允许拓展。(done)
4. 设计一套管理ui(todo)


 [博客](http://blog.gg-workshop.com/) 

 [My-github](http://github.com/winkidney)

by winkidney 2014-05-15


