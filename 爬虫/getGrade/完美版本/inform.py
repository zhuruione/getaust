from student import Student
from excel import *
class Sheet():
    def __init__(self,name,worksheet):
        self.row=2
        self.name=name
        self.gradetype={}
        self.worksheet=worksheet



class inform():
    """信息类"""
    def __init__(self):
        self.workbook=openpyxl.Workbook()
        self.sheets= []
        self.info=get_student_info()
        self.index = 1

    def getinfo(self):
        if self.info:
            inf=self.info.pop()
            return inf
        else:
            return False


    def setInfo(self,data,stu):
        flag=False

        if self.sheets:
            for sheet in self.sheets:
                if sheet.name==stu.classname:
                    flag=sheet

        if flag:
            #说明已经存在该班级的sheet
            write_student_info(flag,data,stu.name)
        else:
            #新建sheet
            newsheet=self.workbook.create_sheet(stu.classname)
            sheet=Sheet(stu.classname,newsheet)
            self.sheets.append(sheet)
            write_student_info(sheet,data,stu.name)
    def over(self):
        saveExcel = "全校成绩.xlsx"
        self.workbook.save(saveExcel)  #一定要记得保存