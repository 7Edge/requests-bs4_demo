#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: github
# Date: 5/7/2019
import requests
from bs4 import BeautifulSoup

# 要爬去github登陆后的内容。那么首先得绕过反爬虫登陆。
# github得登陆需要带上csrf_token所以得拿到登陆得csrftoken，也就是要先爬取github登陆页面获取到csrf_token

# 1. 爬去登陆页面
res_login_page = requests.get(url='https://github.com/login')
# 2. 获取cookie
res_login_cookie = res_login_page.cookies.get_dict()
# 3. 获取csrf_token
soup = BeautifulSoup(markup=res_login_page.text, features='html.parser')
form = soup.find(name='form')
csrf_token = form.find(name='input', attrs={'name': 'authenticity_token'}).attrs.get('value')

# 4. 进行登陆
res_to_login = requests.post(url='https://github.com/session',
                             cookies=res_login_cookie,
                             data={
                                 'commit': 'Sign in',
                                 'utf8': '✓',
                                 'authenticity_token': csrf_token,
                                 'login': '7Edge',
                                 'password': 'gitHub19901204',
                                 'webauthn-support': 'supported'
                             })
# 5. 登陆返回的cookie拿到,然后更新到res_login_cookie中去
res_to_login_cookie = res_to_login.cookies.get_dict()
res_login_cookie.update(res_to_login_cookie)
print(res_login_cookie)

# 5. 登陆后，利用登录页的cookie爬去配置页中的邮箱地址信息
res_settings = requests.get(url='https://github.com/settings/profile?_pjax=%23js-pjax-container',
                            cookies=res_login_cookie)
settings_soup = BeautifulSoup(markup=res_settings.text, features='html.parser')


settings_form = settings_soup.find(name='form', attrs={'class': 'edit_user'})

email = settings_form.find(name='option', attrs={'selected': 'selected'})

print(email.text)
print(res_to_login.status_code)
print(res_to_login.cookies.get_dict())
print(csrf_token)
print(res_login_cookie)

if __name__ == '__main__':
    pass
