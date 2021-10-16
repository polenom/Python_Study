def MySortedBuble(Mylist):
    Mylen = len(Mylist)
    for i1 in range(Mylen):
        for i in range(1,Mylen):
            if Mylist[i-1] > Mylist[i]:
                Mylist[i-1] , Mylist[i] = Mylist[i] , Mylist[i-1]
                i1 = -1
        if i1 != -1:
            break
    return Mylist

print(MySortedBuble(list(map(int, input().split()))))
