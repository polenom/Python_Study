res = [0,0]
a2,a3 = 0,0
with open("input.txt") as f:
    for i in f:
        for alh in i:
            if i.count(alh) == 2:
                res[0] = 1
            elif i.count(alh) == 3:
                res[1] = 1
        if res[0] == 1: a2+=1
        if res[1] == 1 : a3+=1
        res=[0,0]

with open("input.txt") as f:
    x = [ i[:-1] for i in f]
pob= []
for i in range(0,len(x)):
    for i1 in range(i+1,len(x)):
        res = 0
        for n, alh in enumerate(x[i]):
            if x[i1][n] != alh:
                res+=1
        if res == 1:
            pob.append(x[i])
            pob.append(x[i1])
with open('result.txt','w') as f:
    f.write(str(a2*a3)+'\n')
    f.write(pob[0]+'\n'+pob[1])
