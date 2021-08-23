def rev():
    res = str()
    x = input()
    if x != '0':
        res = rev()
    res = res + x + '\r\n'
    return res

print(rev())
