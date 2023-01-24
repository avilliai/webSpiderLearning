from bs4 import BeautifulSoup
if __name__ == '__main__':
    # 从本地导入html数据
    fp=open('D:\python\webSpider\day1\search.html','r',encoding='utf-8')
    # 实例化对象
    soup=BeautifulSoup(fp,'lxml')
    print(soup)
    # 从外部导入html数据
