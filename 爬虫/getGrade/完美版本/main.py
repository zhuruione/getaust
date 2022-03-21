from pool import threadpool
from inform import inform
if __name__ == '__main__':
    inf=inform()
    threadpool=threadpool(11,inf)
    threadpool.runpool()
    for t in threadpool.pool:
        t.join()
    inf.over()

