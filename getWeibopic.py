import requests
import sys
import json

def getHtml(url):
    html = requests.get(url).json()
    if html['ok'] == 1:
        for i in range(1,10):
            try:
                pics = html['data']['cards'][i]['mblog']['pics']
                for pic in pics:
                    url = pic['large']['url']
                    f.write(url)
                    f.write('\n')
                    print(url)
            except KeyError:
                pass
            except IndexError:
                pass
    else:
        sys.exit(0)

if __name__ == '__main__':
    UID = input('请输入微博UID：')
    baseurl = 'https://m.weibo.cn/api/container/getIndex?containerid=107603'+UID+'&page=%s'
    page = 1
    with open('url.txt','a+') as f:
        while True:
            url = baseurl % str(page) 
            page +=1
            getHtml(url)

