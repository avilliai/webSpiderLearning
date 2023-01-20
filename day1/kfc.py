import json
import requests
if __name__ == '__main__':
    city=input('city:')
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    params={'cname':'',
            'pid':'',
            'keyword':city,
            'pageIndex':'1',
            'pageSize':'10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55'
    }
    response=requests.post(url,params=params,headers=headers).json()
    fp=open('./kfc.json','w',encoding='utf-8')
    json.dump(response,fp)
    print(response)
    '''response=requests.post(url,params=params,headers=headers).text
    print(response)'''


