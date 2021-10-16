def MySortMerge(Mylist):
    if len(Mylist) == 2:
        return [Mylist[1]]+[Mylist[0]] if Mylist[0] > Mylist[1] else Mylist
    if len(Mylist) == 1:
        return Mylist
    else:
        x=MySortMerge(Mylist[:len(Mylist)//2])
        y=MySortMerge(Mylist[len(Mylist)//2:])
        res = []
        while x or y:
            if x and y: res.append(y.pop(0) if x[0] > y[0] else x.pop(0))
            elif x and not y: res.append(x.pop(0))
            else: res.append(y.pop(0))
        return res








print(MySortMerge(list(map(int, input().split()))))
