#!/usr/bin/env python
#coding:utf-8
#WeiLib/plugin/acitvity.py - activity plugin for WeiLib
#ver 0.1 by winkidney 2014.05.10
from WeiLib.plugin import activity

#将在每个response返回之前运行，用于修改respose内容。


plugin_text = ( activity,
             )

#每个request收到后的插件，将在收到request的时候运行
plugin_before = ()