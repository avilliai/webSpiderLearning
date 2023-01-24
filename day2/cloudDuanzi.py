import requests
import json
# 爬取网易云段子
if __name__ == '__main__':
    # 使用的url
    url='https://www.yduanzi.com/duanzi/getduanzi'
    # 进行ua伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    #执行访问
    response=requests.post(url,headers=headers).text
    # 字符串转字典
    joke=json.loads(response)
    print(joke.get('duanzi'))
