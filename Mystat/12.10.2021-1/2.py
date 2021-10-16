def MySortedInsertion(Mylist):
    res = [Mylist[0]]
    for num, i in enumerate(Mylist[1:]):
        if Mylist[num] > Mylist[num+1]:
            res = [ i1   for i1 in res if i1 < Mylist[num+1]] +[Mylist[num+1]] + [ i1   for i1 in res if i1 > Mylist[num+1]]
        else: res.append(Mylist[num+1])
    return res
print(MySortedInsertion(list(map(int, input().split()))))
