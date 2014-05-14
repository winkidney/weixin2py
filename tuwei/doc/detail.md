#实现细节

这个文档描述部分实现细节

##菜单构成
* 过往活动 （点击进入过往活动历史）
  * 智能硬件    自定义菜单事件     消息KEY：VIEW_SMART_HARDWARE   （返回一条消息）
  * 移动互联    自定义菜单事件     消息KEY：VIEW_MOBILE_COMMUNICATION    （返回一条消息）
  * 技能互换    自定义菜单事件     消息KEY：VIEW_SKILL_SWAP   （返回一条消息）
  * 户外  自定义菜单事件     消息KEY：VIEW_OUTDOOR  （返回一条消息）
* 活动
  * 近期活动    自定义链接 URL:http://weixin2py.gg-workshop.com/recent/  （跳转到网址）
  * 技能互换    自定义链接 URL:http://weixin2py.gg-workshop.com/swap/    （跳转到网址）
  * 我来组织    自定义菜单事件     消息KEY：CREATE_ACTIVITY   （返回一条消息，内含有一条指定用户id的网址）
* 我们
  * 微信功能    自定义菜单事件     消息KEY：ABOUT_WEIXIN  （返回一条消息）
  * 了解突围    自定义菜单事件     消息KEY：ABOUT_TUWEI   （返回一条消息）
  * 成员介绍    自定义菜单事件     消息KEY：ABOUT_MEMBERS （返回一条消息）
  * 加入我们    自定义菜单事件     消息KEY：JOIN_US  （返回一条消息）
