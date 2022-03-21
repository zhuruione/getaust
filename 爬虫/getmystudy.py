import threading
from http.client import HTTPResponse

from bs4 import BeautifulSoup #网页解析
import re  #正则表达式
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行sqllite数据库操作
if __name__ == '__main__':
    url='https://jianghu.live2008.com/jiexi/?url=https://v7.dious.cc/20211004/xZuy1AKM/index.m3u8###'
    req = urllib.request.Request(url)
    rep = urllib.request.urlopen(req)
    print(rep.read().decode('utf-8'))



