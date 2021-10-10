hod = 1
pole = [[0,0,0] for i in range(3)]
try:
    while list(filter(lambda a: True if 0 in a else False , pole)):
        while True:
            try:
                x , y = map(int, input('Input x,y  %s plaer :' %hod ).split())
                if pole[x-1][y-1] != 0:
                    raise ValueError
            except ValueError:
                print('Don\'t true number ')
            else:
                break
        pole[x-1][y-1] = 1 if hod == 1 else 2
        for i in pole:
            print('| '.join(map(str, i.copy())).replace('0', ' ').replace('1','x').replace('2','o'))
            (print('- - - -')) if i != pole[2] else 1
        for i in range(3):
            if pole[i].count(hod)== 3 or [ i1[i] for i1 in pole].count(hod) == 3 or [ i1[num] for num,i1 in enumerate(pole)].count(hod) == 3 or [ i1[2 - num] for num,i1 in enumerate(pole)].count(hod) == 3:
                print('Win %s ' %hod)
                raise ValueError
        hod = 2 if hod == 1 else 1
    else:
        print('Win frendly')
except ValueError:
    pass

