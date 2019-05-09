#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: lagouwang
# Date: 5/8/2019
import requests
from bs4 import BeautifulSoup


# 拉勾网通过爬虫登陆
# 登陆反爬虫手段：
# 1. 必须带上user-agent请求头：说明客户端时浏览器发起的
# 2. cookie从登陆页面开始才时合法cookie： 认证请求必须带上访问页面时的cookie，即使认证成功但是返回的cookie时假的反爬虫cookie。
# 3. 从登陆前的访问会话已经开始，并且后续的访问都是在后端会话中绑定了随机反爬虫数据（后端会对每次带上会话cookie的请求进行验证绑定的随机信息）
#    如果时爬虫，那么如果只是拷贝浏览器端的是不行的，因为没有拷贝cookie信息，爬虫的cookie后端会话和随机串绑定不上。
# 如：
# 4. referer 可以防止盗链，浏览器行为（爬虫不会自动带）对于引入文件的请求都会带上referer字段，给资源使用。所以登陆访问有问题
# 5. host 是浏览器行为（爬虫不会自动带），会带上访问的网站的名称。这个主要是给web server提供了多个网站来区分将请求发送给哪个网站处理。
# 6. 带滑动验证的。



if __name__ == '__main__':
    pass
