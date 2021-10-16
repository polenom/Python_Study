def MySortedInsertion(Mylist):
    res = [Mylist[0]]
    for num, i in enumerate(Mylist[1:]):
        if Mylist[num] > Mylist[num+1]:
            res = [ i1   for i1 in res if i1 < Mylist[num+1]] +[Mylist[num+1]] + [ i1   for i1 in res if i1 > Mylist[num+1]]
        else: res.append(Mylist[num+1])
    return res
def MySortTwo(Mylist):
    return Mylist[:len(Mylist)//2]+Mylist[len(Mylist)//2:][::-1]
print(MySortTwo(list(map(int, input().split()))))
