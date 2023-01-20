import requests
import json
if __name__ == '__main__':
    url='https://www.yduanzi.com/duanzi/getduanzi'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response=requests.post(url,headers=headers).text
    joke=json.loads(response)
    print(joke.get('duanzi'))
