import random
def binarSeatch(MyNumber, MyList):
    res = len(MyList)//2
    num =0
    while 2**num <= len(MyList):
        num +=1
        if MyList[res] == MyNumber:
            return res
        elif MyNumber > MyList[res]:
            res = res +(len(MyList) - res)//2
        elif MyNumber < MyList[res]:
            res = res//2
    return None
def MySortQuick(Mylist):
    if len(Mylist) == 1 or len(Mylist) == 0:
        return Mylist
    else:
        j = 0
        i = len(Mylist) - 1
        for number in range(i):
            if Mylist[i] < Mylist[j] :
                if i > j:
                    Mylist[i], Mylist[j] = Mylist[j],Mylist[i]
                    i , j = j+1 , i
                else:
                    i+=1
            elif Mylist[i] > Mylist[j]:
                if i > j:
                    i -= 1
                else:
                    Mylist[i], Mylist[j] = Mylist[j], Mylist[i]
                    i, j =j-1, i
            else:
                i += -1 if i > j else 1
        return MySortQuick(Mylist[:j])+[Mylist[j]]+MySortQuick(Mylist[j+1:])

x = [ random.randrange(100) for i in range(0,11)]
x = MySortQuick(x)

print(x)
while True:
    print('Input number')
    res = binarSeatch(int(input()), x)
    if res == None:
        print('Not number in list')
    else:
        print(res)
        break
