def OutStars(a):
    if a == 1:
        return print('*', end='')
    else:
        OutStars(a-1)
        return print('*', end='')
OutStars(int(input('Input number = ')))

