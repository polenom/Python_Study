import random
def listSeatch(MyNumber, MyList):
    x = [num for num, i in enumerate(MyList) if i == MyNumber]
    return x[0] if x else None


x = [ random.randrange(100) for i in range(0,11)]
print(x)
while True:
    print('Input number')
    res = listSeatch(int(input()), x)
    if res == None:
        print('Not number in list')
    else:
        print(res)
        break
