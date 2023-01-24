import requests
import json
import re
if __name__ == '__main__':
    url='https://suulnnka.github.io/BullshitGenerator/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    rule='let .*? = [(.*?)]'

    response=requests.get(url,headers).text
    text = re.findall(rule, response, re.S)
    print(text)
    with open('./generate.txt','w',encoding='utf-8') as fp:
        fp.write(str(text))
