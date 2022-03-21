from http.client import HTTPResponse

from bs4 import BeautifulSoup #网页解析
import re  #正则表达式
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行sqllite数据库操作
from test.gethead import gethead


def get_html(url,head):

    req=urllib.request.Request(url,headers=head)
    try:
        rep=urllib.request.urlopen(req,timeout=1)  #type:HTTPResponse
        print(rep.headers)
        html=rep.read().decode('utf-8')
        return html
    except urllib.error.URLError as e:
        print(url,'无法访问',e.reason)
        return False

def get_href(html):
    bs=BeautifulSoup(html,'html.parser')
    all_a=bs.select('a')
    href=[]
    for a in all_a:
        a_attrs=a.attrs
        if 'href' in a_attrs:
            if a_attrs['href'].startswith('http'):
                href.append(a_attrs['href'])
            else:
                href.append()
    return href

def write(text):
    try:
        with open('test.txt','a',encoding='utf-8') as test:
            test.write('\n')
            print(text)
            test.write(text)
            test.close()
            return 1
    except:
        print("写入失败")
        return 0

#进行无限爬取
def search(hrefs,has_searched,n):
    if n>4:
        print('=================================\n\n爬取结束')
        return
    for each in hrefs:
        if each not in has_searched:
            try:
                write(each)
                html = get_html(each)
                hrefs = get_href(html)
                has_searched.append(each)
                search(hrefs,has_searched,n+1)
            except:
                pass

if __name__ == '__main__':
    head = gethead('head.txt')
    hasw=[]
    n=1
    url='http://jwgl.aust.edu.cn/eams/teach/grade/course/person!search.action?semesterId=140&projectType='
    html=get_html(url,head)
    hrefs=get_href(html)
    search(hrefs,hasw,n)