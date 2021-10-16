class Book:
    def __init__(self, name = None, author = None, publishing = None, genre = None,year = None ):
        self.name = name
        self.author = author
        self.publishing = publishing
        self.genre = genre
        self.year = year

class Student:
    def __init__(self, lastname = None, firstname = None, year = None, phonenumber = None,numbergroup = None, numbersemester = None, formeducation = None,data = None):
        self.data = data
        self.lastname = lastname
        self.firstname = firstname
        self.year = year
        self.phonenumber = phonenumber
        self.numbergroup = numbergroup
        self.numbersemester = numbersemester
        self.formeducation = formeducation

    def setInfo(self):
        for k,v in self.__dict__.items():
            if k == 'data' and self.__dict__[k] != None:
                for k1,v1 in self.__dict__[k].items():
                    print('%s -> %s input new vault : ' % (k1.upper(), v1), end='')
                    res = input()
                    self.__dict__[k][k1] = v1 if res == '' else res
            elif k == 'data':
                print('Input new data in form \' math 3 langue 4\': ', end = '')
                res = input().split()
                self.__dict__[k]= {i:res[num*2+1] for num,i in enumerate(res[::2])}
            else:
                print('%s -> %s input new vault : ' %(k.upper(), v), end= '')
                res = input()
                self.__dict__[k] = v if res == '' else res
    def printInfo(self):
        for k,v in self.__dict__.items():
            if k == 'data':
                print('Items with marks')
                for k1,v1 in self.__dict__[k].items():
                    print('%s: %s' %(k1,v1))
            else:
                print('%s: %s' %(k.upper(), v))
    def getRating(self):
        if self.data == None:
            print('None')
        else:
            print(sum(self.data.values())/len(self.data))
    def getCourseList(self, bal):
        for k,v in self.data.items():
            if v > bal:
                print(k)

def listStudentForm(*args, form):
    for i in args:
       if i.formeducation  == form:
           print(i.firstname, i.lastname)
def listStudentSort(*args):
    for i in sorted([i.lastname for i in args]):
        print(i)

