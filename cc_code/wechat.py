#!/usr/bin/python
# -*- coding: UTF-8 -*-

import itchat
itchat.login()
#给文件传输助手发信息
itchat.send(u'你..', 'filehelper')

#获取所以朋友信息
#friends = itchat.get_friends(update=True)[0:]

#给曹晶晶发信息，通过备注名'曹晶晶'找到对应username
users = itchat.search_friends(name=u'曹晶晶')
#print(users)
userName = users[0]['UserName']
itchat.send(uu'该起来动一下了',toUserName = userName)
print('succeed')
