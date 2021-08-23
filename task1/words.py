vvod = str()
resslovar = dict()
res= dict()
for i in range(int(input())):
    for i in input():
        if i in [',', ':', '.','!','?']:
            continue
        else:
            vvod += i
    vvod += ' '
for i in vvod.lower().split():
    if i in resslovar:
        resslovar[i] += 1
    else:
        resslovar[i] = 1
for key, item in resslovar.items():
    if item in res:
        res[item].append(key)
    else:
        res[item]= [key]
for i in sorted(res.keys(), reverse=True):
    for i1 in sorted(res[i]):
        print(str(i1))
