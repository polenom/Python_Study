def myCount(Mytuple):
    from collections import defaultdict
    mydict = defaultdict(int)
    for i in Mytuple:
        mydict[len(str(i))]+=1
    for i in sorted(mydict.keys()):
        print('{} ==> {}'.format(i, mydict[i]))
import random
x = (random.randrange(10000)for i in range(1000))
myCount(x)
