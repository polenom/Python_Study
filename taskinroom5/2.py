def chocolate(a,b,c):
    if (c%a == 0 or c%b == 0) and a*b>=c:
        print('YES')
    else:
        print("NO")
a = int(input())
b= int(input())
c = int(input())
chocolate(a,b,c)

res = 0
for i in range(10):
    res+=int(input())
print(res)

res = 0
for i in range(10):
    res+=int(input())
print(res)

res= ''
for num,i in enumerate(input()):
    if num%3 !=0:
        res+=i
print(res)
