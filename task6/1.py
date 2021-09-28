x =list(map(int, input().split()))
for i in range(1,len(x)):
    if x[i-1] < x[i]: print(x[i], end =' ')
