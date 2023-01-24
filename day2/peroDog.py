import requests
import json
import re
if __name__ == '__main__':
    url='https://we.dog/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    # 执行访问
    response = requests.get(url, headers=headers).text
    print(response)
    rule=r'<section class=border-1><article>(.*?)</article><address></address></section>'
    text=re.findall(rule,response,re.S)
    print(text)
