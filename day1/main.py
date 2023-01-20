import requests
'''(requests编码流程)
    指定url
    发起请求
    获取响应数据
    持久化存储
'''

if __name__ == '__main__':
    url = "https://www.bilibili.com/?spm_id_from=333.337.0.0"
    # get方法会返回一个响应对象
    response=requests.get(url=url)
    # 获取响应数据，返回的响应对象拥有text方法
    page=response.text
    print(page)
    with open('bilibili.html', 'w', encoding='utf-8') as fp:
        fp.write(page)
    print("over")