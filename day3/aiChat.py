import requests
import json

from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url='https://www.ai-topia.com/mr/chat/sendChat'
    headers = {
        'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxMDc4OCwidXNlcl9rZXkiOiJiN2Y5NGFjMGYwM2Y0M2Q4YjY1ZWZkOTBlZmFiYTVhMCIsInVzZXJuYW1lIjoiMDFNMmFsdCJ9.H6e07 - pz8WX8ghaawKnZMmfU9BOlmN0TKqDh6jxPnoMkoI11myn1rlmGzMCSNnSI6q1u_PY1O09joYpvY3aF3w',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'
    }
    data={"content":"你好","roleId":1797}
    response=requests.post(url,headers=headers,data=data,verify=False).json()
    print(response)