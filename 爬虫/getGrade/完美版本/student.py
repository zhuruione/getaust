class Student:
    def __init__(self,id,password):
        self.id=id
        self.password=password
        self.data=None
        self.classname=None
        self.headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    }
        self.name=''
        self.grade={}
    def set_cookie(self,cookies):
        self.headers['Cookie']=cookies
    def set_data(self,data):
        self.data=data