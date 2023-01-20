import requests
import json
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'
    params={'type':'11',
            'interval_id':'100:90',
            'action':'',
            'start':'20',
            'limit':'20'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response=requests.get(url,params=params,headers=headers).json()

    fp=open('./douban.json','w',encoding='utf-8')
    json.dump(response,fp)
    print(response)
    print('over')
