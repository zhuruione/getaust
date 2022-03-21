import threading
from gethtml import *
from excel import *
from inform import inform

class Gradethread(threading.Thread):
    """执行线程"""
    def __init__(self,informtion,lock,id):
        super().__init__()
        self.id=id
        self.lock_read=lock['read']#type:threading.Lock
        self.lock_write=lock['write']#type:threading.Lock
        self.inf=informtion#type:inform

    def run(self):
        print(self.id+'启动')
        while True:
            #获取一个学生账号密码
            self.lock_read.acquire()
            stu = self.inf.getinfo()
            self.lock_read.release()

            if not stu:
                print(self.id+'运行结束')
                break

            #开始爬取数据
            try:
                inf_html = get_rep(stu)  # type:HTTPResponse
                login(inf_html, stu)
            except BaseException as e:
                print(stu.id,'登录失败',e)
                continue

            try:
                html = get_grade_html(stu)
                data = data_soup(html)
            except BaseException as e:
                print(stu.name+'获取分数失败',e)
                continue

            #写入数据
            self.lock_write.acquire()
            print(self.id, '开始写入', stu.id)
            try:
                print(self.inf.index)
                self.inf.setInfo(data,stu)
                self.inf.index += 1
            except:
                print('写入数据出错')
            self.lock_write.release()

