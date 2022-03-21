from bs4 import BeautifulSoup
import urllib.request
from http.client import HTTPResponse
import re

def href_is_exits(tag):
    return tag.has_attr('href')
if __name__ == '__main__':
    url='http://www.baidu.com'
    req=urllib.request.Request(url=url)
    rep=urllib.request.urlopen(req)   #type:HTTPResponse
    html=rep.read().decode('utf-8')
    bs=BeautifulSoup(html,'html.parser')


    # all_a=bs.find_all(text=re.compile('\da1'))
    # for each in all_a:
    #     print(each)
    all_a=bs.select("body > div >")
    print(all_a)
    for each in all_a:
        print(each)