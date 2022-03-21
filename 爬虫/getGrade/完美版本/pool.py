from inform import inform
import threading

from mythread import Gradethread


class threadpool():
    """将线程统一管理"""
    def __init__(self,maxsize,inf):
        self.inf=inf
        self.lock={}
        self.lock['read']=threading.Lock()
        self.lock['write']=threading.Lock()
        self.maxsize=maxsize
        self.pool=[]
        id=1
        for thread in range(1,self.maxsize):
            thread=Gradethread(self.inf, self.lock, 'gthread--' + str(id))
            self.pool.append(thread)
            id+=1
    def runpool(self):
        for each in self.pool:
            each.start()
