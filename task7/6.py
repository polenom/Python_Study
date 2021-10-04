def capitalize(x):
    res = str()
    for i in x.split():
        res+=chr(ord(i[0])-32)+i[1:]+' '
    return res[:-1]

print(capitalize(input()))
