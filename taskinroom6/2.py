def Vek(god):
    with open('5/data.txt') as f:
        for i in f:
            if i.lstrip().startswith(god):
                return i[:-1]
        return "Нет такого года"
res= []
while True:
    vvod = input('Введите год: ')
    if vvod == 'q':
        break
    elif not vvod.isdigit():
        with open("5/%s" % vvod, 'w') as f:
            for i in res:
                f.write(i+'\n')
        break
    else:
        r = Vek(vvod)
        print(r)
        if r == "Нет такого года":
            continue
        res.append(r)
