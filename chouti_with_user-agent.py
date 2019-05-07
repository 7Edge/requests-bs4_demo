#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: chouti
# Date: 5/7/2019
import requests
from bs4 import BeautifulSoup

# 爬去抽屉新热榜（需要携带header: agent才行）
res_index = requests.get(url="https://dig.chouti.com/", headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
})

soup = BeautifulSoup(markup=res_index.text, features='html.parser')
# 拿到首页内容列表标签
content_list = soup.find(name='div', attrs={'class': 'content-list',
                                            'id': 'content-list'})
timeintopool = content_list.find(name='div', attrs={'class': 'timeIntoPool'})
print(timeintopool.text)
item_list = content_list.find_all(name='div', attrs={'class': 'item'})

for item in item_list:
    a_tag = item.find(name='a', attrs={'class': 'show-content color-chag'})

    print(a_tag.text.strip())

if __name__ == '__main__':
    pass
