import random
n = int(input())
otvet = random.randrange(1,n+1)
pom = set(i for i in range(1,n+1))
while len(pom) != 1:
    vvod =input().split()
    if vvod[0] == 'HELP':
        print(str(pom)[1:-1])
    else:
        vvod = set(map(int, vvod))
        if otvet in vvod:
            pom = pom & vvod
            print('YES')
        else:
            pom = pom - vvod
            print('NO')
print('YOU WIN')
