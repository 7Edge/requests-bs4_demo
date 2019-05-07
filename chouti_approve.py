#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: chouti_approve
# Date: 5/7/2019

import requests
from bs4 import BeautifulSoup

# 抽屉新热由于对爬虫进行了一些防范，登陆时返回的cookie时无效的，他是根据他自己的业务展现，来放置爬虫程序。
# 用户登陆前，肯定是先是到达它的首页，再登陆，所以它的登陆会话再首页时就开始，只不过则是的cookie记录的会话id才是真实的。而直接获取登陆视图返回的cookie
# 是一个不全的cookie，这是个伪造的cookie，所以要通过爬虫点赞某个文章，就需要先爬去首页，获取cookie，然后登陆，最后点暂时使用首页时获取的cookie进行登陆
# 相当于用户登陆时如果没有携带cookie，那这次请求不是用户出发的时爬虫；如果携带了cookie，我在后台通过cookie有会话，那么我就再这个会话中存储用户登陆
# 成功的信息；然后构建一些假的cookie返回给客户端。对于这种情况只需用第一次的cookie带上进行登陆，登陆成功后，后面就都是用第一次cookie进行访问。

# 访问首页拿到cookie
res_index = requests.get(url='https://dig.chouti.com/',
                         headers={
                             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'})

r1_cookie = res_index.cookies.get_dict()
print(r1_cookie)

# 登陆带上cookie，后端认证成功对cookie
res_login = requests.post(url='https://dig.chouti.com/login',
                          headers={
                              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
                          },
                          data={
                              'phone': '8615198138198',
                              'password': '138198',
                              '8615198138198': '1'
                          },
                          cookies=r1_cookie)

print(res_login.text)

# 再次发送请求进行点赞某一个item
res_approve = requests.post(url='https://dig.chouti.com/link/vote?linksId=25983911',
                            headers={
                              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
                            },
                            cookies=r1_cookie)

print(res_approve.text)

if __name__ == '__main__':
    pass
