import json

import requests
if __name__ == '__main__':
    post_url='https://fanyi.baidu.com/sug'
    word=input('key:')

    data={'kw':word}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    #确认响应数据是json时调用.json方法
    response=requests.post(url=post_url,data=data,headers=headers).json()
    print(response)
    fp=open('./'+word+'.json','w',encoding='utf-8')
    json.dump(response,fp=fp)
