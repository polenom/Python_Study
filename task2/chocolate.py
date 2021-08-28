N = int(input())
M = int(input())
K = int(input())
if (K%N==0 and N*M>K) or (K%M==0 and N*M>K):
    print("YES")
else:
    print("NO")

