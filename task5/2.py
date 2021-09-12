N = int(input())
res =1
while 2**res <= N:
    res+=1
print(res-1, 2**(res-1))    
