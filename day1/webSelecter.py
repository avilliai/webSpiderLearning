import requests
if __name__ == '__main__':
    keyw=input('text:')
    url="https://cn.bing.com/search?q="+keyw
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    '''param={'query':keyw}
    response=requests.get(url=url,params=param).text'''
    response=requests.get(url,headers=headers).text
    with open("./search.html","w",encoding='utf-8') as fp:
        fp.write(response)