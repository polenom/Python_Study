n =int(input())
res= list()
while n != 0:
    res.append(n)
    n =int(input())
print(res.count(max(res)))
