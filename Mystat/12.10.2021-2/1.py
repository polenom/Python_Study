def MySortShalle(Mylist):
    d = len(Mylist)//2
    Mylen = len(Mylist)
    while d >= 1:
        for i in range(0,Mylen):
            if i+d < Mylen and Mylist[i] > Mylist[i+d]:
                Mylist[i], Mylist[i+d] = Mylist[d+i],Mylist[i]
                i -= d
                while i >=0:
                    if i + d < Mylen and Mylist[i] > Mylist[i + d]:
                        Mylist[i], Mylist[i + d] = Mylist[d + i], Mylist[i]
                    else:
                        break
                    i -= d
            elif not i+d < Mylen:
                break
        d //=2

    return Mylist







print(MySortShalle(list(map(int, input().split()))))
