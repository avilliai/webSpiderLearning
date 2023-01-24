# -*- coding: utf-8 -*-
#爬取水浒传
import re

import requests
from bs4 import BeautifulSoup
import json
if __name__ == '__main__':
    bookname=input('输入书名')
    #url='https://www.zhonghuadiancang.com/wenxueyishu/shuihuzhuan/'
    url='https://www.zhonghuadiancang.com/waiguomingzhu/15136/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'GBK'
    response.encoding = 'utf-8'

    soup=BeautifulSoup(response.content,'lxml')
    da=soup.select('#booklist > li >a')
    print(da)
    for i in da:
        print(i)
        rule='<a href="(.*?)"'
        text=re.findall(rule,str(i),re.M)
        print(text[0])
        #print(i.string)
        #print(i.a['href'])
        response=requests.get(url=text[0],headers=headers)
        response.encoding = 'GBK'
        response.encoding = 'utf-8'
        soup1=BeautifulSoup(response.content,'lxml')
        data=soup1.select('#content>p')

        #with open('./水浒.txt', 'a', encoding='utf-8') as fp:
            #fp.write(i.string + '\n')

        for para in data:
            with open('./'+bookname+'.txt', 'a',encoding='utf-8') as fp:
                fp.write(str(para.string)+'\n')
        print('写入完成\n'+'-------------------')

    # v > p:nth-child(2) > a:nth-child(3)
    # v > p:nth-child(2) > a:nth-child(4)


