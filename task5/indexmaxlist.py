n, s = int(input()), list()
while n != 0:
    s.append(n)
    n = int(input())
print(s.index(max(s)))
