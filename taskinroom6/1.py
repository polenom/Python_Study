
def poisk(puti):
    res = {}
    with open(puti) as f:
        for stroki in f:
            for word in stroki.split():
                slovo = ''
                for alh in word:
                    if alh.isalpha():
                        slovo+=alh.lower()
                    if not word.startswith('-') and not word.startswith('-') and alh in ['-']:
                        slovo+=alh
                    if alh in ["'"]:
                        slovo+=alh
                if slovo == '':
                    continue
                if slovo in res:
                    res[slovo] += 1
                else:
                    res[slovo] = 1
    return res
def MaxSpisok(res, n):
    res = [[k,v] for k,v in res.items()]
    return sorted(res,key=lambda a:a[1],reverse=True)[:n]

def Ch(res, n):
    myres =[]
    for k,v in res.items():
        if v == n:
            myres.append(k)
    return myres
def Fil(put, sl):
    with open(put, 'w') as f:
        for i in sorted(sl.items(),key=lambda k: k[1] , reverse=True):
            f.write(str(i[0])+' => '+str(i[1])+'\n')
