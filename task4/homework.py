import random
res = list()
for i in range(15):
    res.append(random.randrange(1000))
print(res)
mi = 1000
ma = 0
su = 0
for  num, i in enumerate(res):
    su += i
    if i < mi:
        mi = i
        miin = num
    if i > ma:
        ma = i
        main = num
res[miin], res[main] = ma, mi
print(mi, ma , su , sep ='\n' )

print(res)
x = [res[int(input('Введите индекс (0...15): '))] for i in range(3)]
print(sum(x),x,'Человечество')
com = [random.randrange(1000) for i in range(3)]
print(sum(com),com, 'AUTOMATON2000')
if sum(x) > sum(com):
    print('победа человека')
elif sum(x) == sum(com):
    print('у человечества есть шанс')
else:
    print('Все беда')
