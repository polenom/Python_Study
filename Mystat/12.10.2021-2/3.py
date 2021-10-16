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

print(MySortPiramida(list(map(int, input().split()))))
