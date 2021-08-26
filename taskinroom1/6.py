def sc(a,b,c):
    D=b**2-4*a*c
    if D < 0:
        return None,None
    elif D == 0:
        return -b/2*a
    x1=(-b+D**0.5)/2*a
    x2=(-b-D**0.5)/2*a
    return round(x1,2),round(x2,2)
a,b,c = map(int, input().split())
print(sc(a,b,c))
