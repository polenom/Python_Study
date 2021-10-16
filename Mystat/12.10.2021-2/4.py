def MyOladi(Mylist):
    res = 0
    Mylen = len(Mylist)
    Mysort = sorted(Mylist)
    Shift = Mylen
    while Mysort != Mylist:
        MyIndex = Mylist[:Shift].index(max(Mylist[:Shift]))
        Mylist = Mylist[:MyIndex+1][::-1]+Mylist[MyIndex+1:]
        res+= 0 if MyIndex == 0 else 1
        if Mysort == Mylist:
            break
        Mylist= Mylist[:Shift][::-1]+Mylist[Shift:]
        Shift-=1
        res+=1
    return  res

print(MyOladi(list(map(int, input().split()))))
