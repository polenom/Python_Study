N, N1 = map(int, input().split())
if N%N1 == 0:
    print('Число {0} делится на число {1} без остатка'.format(N,N1))
else:
    print('Число {0} делится на число {1} c остатком'.format(N,N1))

