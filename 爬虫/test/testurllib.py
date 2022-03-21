import urllib.parse
from http.client import HTTPResponse
import urllib.request as request
import urllib.error as err

if __name__ == '__main__':

    # try:
    #     data=bytes(urllib.parse.urlencode({'zr':'yyds'}),encoding='utf-8')
    #     response=req.urlopen('http://douban.com',data=data,timeout=3) #type: HTTPResponse
    #     print(response.read().decode('utf-8'))
    # except err.URLError:
    #     print('请求超时')

    url='https://douban.com'
    headers={   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    data=bytes(urllib.parse.urlencode({'zr':'yyds'}),encoding='utf-8')
    req=request.Request(url,headers=headers,method='GET')
    rep=request.urlopen(req) #type:HTTPResponse
    text=rep.read().decode('utf-8')
    print(text)

