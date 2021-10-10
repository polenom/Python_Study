import random
def FindMin(lis):
    if len(lis) == 10:
        return lis
    else:
        x = FindMin(lis[1:])
        if sum(lis[:10]) < sum(x):
            return lis[:10]
        else:
            return x


print(FindMin([random.randrange(100) for i in range(30)]))
