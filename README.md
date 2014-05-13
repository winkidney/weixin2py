#weixin2py--微信公众平台web服务器

### 1.简介

* 使用python2.7和django 1.5.1开发的微信公众平台服务端程序，可以自动回复用户发来微信的消息。
* 最初的启发来自“武大助手”，类似的平台，提供校园信息服务&服务微信化
* 有什么 意见或者建议请发issue

### 2. 特性
* 当用户发来第一条消息的时候，自动检测用户是否存在并生成一个唯一的用户（使用openid），存储到数据库。(新版本中尚未实现)
* 可拔插设计，提供django app ‘WeiLib’，里面有大部分可能用到的工具类和工具函数，需要的时候，新建你的django app，并且在app中使用WeiLib即可。
* 消息模版,WeiLil.llib中包含了text_response和pic_text_response函数，传入参数可以在任意view或者handler中使用.
* 示例应用中将实现一个简单的缓存session功能。更改你的缓存后端或者更改缓存接口即可。
* 新增路由功能((数据库路由和文件路由)，使用正则表达式对回复进行匹配，可以在自己的router.py中定义router规则，类似    
```python
my_router = [
            ('text', re.compile'^关于$', about_handler),
            ]
```
程序会匹配关键字并使用handler返回相应。    

目前新版本开发中，不保证任何可用性，需要老版（代码很丑陋）请移步：[这里](https://github.com/winkidney/weixin2py/tree/release1.0) 

### 3.Change Log
* 2014.05.08 - 全面重构中
* 2013.xx.xx - first release,多么幼稚的代码

### 3.To Do List
1. 简化程序，并将通用处理过程提取出来，让处理函数可以直接方便的处理消息
2. 将用户session改到key-value数据库存储或者内存缓存，提高效率和可靠性。
3. 修改数据库设定，让数据库具有通用性并允许拓展。
4. 设计一套管理ui


 [博客](http://blog.gg-workshop.com/) 

 [My-github](http://github.com/winkidney)

by winkidney 2014-03-12


