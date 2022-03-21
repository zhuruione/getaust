import time
import urllib.parse
import hashlib
from http.client import HTTPResponse
from bs4 import BeautifulSoup #网页解析
import urllib.request as request,urllib.error as urlerror #制定url，获取网页数据

def get_rep(stu):
    """获取会话session和加密字符串"""
    cookies = 'semester.id=140;'
    url = 'http://jwgl.aust.edu.cn/eams/login.action'
    req = request.Request(url, data=stu.data, headers=stu.headers)
    rep = request.urlopen(req)  # type:HTTPResponse
    time.sleep(0.5)
    rep_head=rep.getheaders()
    for each in rep_head:
        if each[0]=='Set-Cookie':
            cookies+=each[1][0:each[1].find(';')+1]
    stu.set_cookie(cookies[0:-2])
    inf_html = rep.read().decode()  # type:HTTPResponse
    rep.close()
    return inf_html



def login(html,stu):
    """实现用户登录"""
    url = 'http://jwgl.aust.edu.cn/eams/login.action'
    html=BeautifulSoup(html,'html.parser')
    js=html.select('script[type="text/javascript"]')
    js=str(js.pop())
    # print(js)
    key=js[js.find("form['password'].value = CryptoJS.SHA1(")+len("form['password'].value = CryptoJS.SHA1('"):js.find("' + form['password'].value);")]

    # print(key)
    password=stu.password
    password=hashlib.sha1((key+password).encode('utf-8')).hexdigest()
    stu.data=bytes(urllib.parse.urlencode({'username':stu.id,
                                           'password':password,
                                           'session_locale':'zh_CN',
                                           'encodedPassword':''}),encoding='utf-8')
    req_login=request.Request(url,headers=stu.headers,data=stu.data)
    rep = request.urlopen(req_login)
    try:
        time.sleep(0.5)
        login_html = rep.read().decode('utf-8')
    except BaseException as e:
        print('!!!!!!!!!!!!!!!!!!!!!')
    rep.close()
    # time.sleep(0.5)
    bs=BeautifulSoup(login_html,'html.parser')
    try:
        a = bs.select("a[href='/eams/security/my.action']")
        name = a[0].text
        stu.name = name[0:name.find('(')]
    except:
        a = bs.select("div[class='ui-state-error ui-corner-all'] > span")
        raise BaseException(a[1].text)
    return login_html

def get_grade_html(stu):
    """获取成绩单"""
    url = 'http://jwgl.aust.edu.cn/eams/teach/grade/course/person!search.action?semesterId=140&projectType='
    req = urllib.request.Request(url, headers=stu.headers)
    rep = urllib.request.urlopen(req)  # type:HTTPResponse
    time.sleep(0.5)
    grade_html=rep.read().decode('utf-8')
    rep.close()
    # time.sleep(0.5)
    #退出登录
    url = 'http://jwgl.aust.edu.cn/eams/logout.action'
    req = urllib.request.Request(url, headers=stu.headers)
    rep=urllib.request.urlopen(req)
    rep.close()
    return grade_html

def data_soup(html):
    """解析成绩单数据"""
    data={}
    soup = BeautifulSoup(html, 'html.parser')
    tr=soup.select('tbody > tr')
    for tds in tr:
        grad=[]
        for td in tds:
            try:
                text=td.text.strip().replace('\t','').replace('\n','')
                if text !='':
                    grad.append(text)
            except:
                pass
        data[grad[3]]=grad[6]
    return data

