def MySortPiramida(Mylist):
    MySet = {num:i for num, i in enumerate(Mylist)}
    def sor(Myli):
        for i in range(len(Myli)//2-1,-1,-1):
            if Myli[i*2+1] > Myli[i]: Myli[i*2+1] ,Myli[i] = Myli[i], Myli[i*2+1]
            if (i*2+2) < len(Myli) and Myli[i*2+2] > Myli[i]: Myli[i*2+2] ,Myli[i] = Myli[i], Myli[i*2+2]
        return Myli
    Mylen = len(Mylist)
    for i in range(Mylen):
        Mylist = sor(Mylist[:Mylen - i])+Mylist[Mylen - i:]
        Mylist[0],Mylist[-1*(1+i)] = Mylist[-1*(1+i)], Mylist[0]
    return Mylist

def MySortPiramida2(Mylist):
    MySet = {num:i for num, i in enumerate(Mylist)}
    Mylen = len(Mylist)
    for i in range(Mylen,0,-1):
        for i1 in range(i//2-1,-1,-1):
            if MySet[i1*2+1] > MySet[i1]: MySet[i1*2+1] ,MySet[i1] = MySet[i1], MySet[i1*2+1]
            if (i1*2+2) < i and MySet[i1*2+2] > MySet[i1]: MySet[i1*2+2] ,MySet[i1] = MySet[i1], MySet[i1*2+2]
        MySet[0], MySet[i-1] = MySet[i-1], MySet[0]

    return [v for k,v in MySet.items()]



print(MySortPiramida(list(map(int, input().split()))))
