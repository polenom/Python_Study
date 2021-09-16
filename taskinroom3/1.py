def division(a, b):
    if a % b == 0:
        print('Division without remainder')
    else:
        print('Division with remainder')


def inplist(a):
    import random
    return a[random.randrange(len(a))]

def nstr(mystr, n):
    return mystr[n]*len(mystr)

def CountRank(a):
    return len(str(int(a)))

def SumNumber(a):
    return sum([int(i)  for i in str(a) ])

def ATMCheck(a):
    return 'can be done' if sum(a) >= 0 else 'can not be commit'

def my_replace(a,b,c):
    res = a[:]
    while b in res:
        res = res[:res.index(b)]+c+res[res.index(b)+len(b):]
    return res

def TitleStr(a):
    res=0
    for i in a:
        if i.isalpha() and ord(i)>=97: res+=1
        elif i.isalpha() and ord(i)<97:res-=1
    return a.lower() if res > 0 else a.upper()

def RemoveStartEnd(a,b):
    return a[:a.find(b)]+a[a.rfind(b)+1:]
