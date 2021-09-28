text=list(map(int, input().split()))
mn = min(text)
mx= max(text)
for i in text:
    if mn == i:
        print(mx, end= ' ')
    elif mx == i:
        print(mn, end=' ')
    else:
        print(i, end= ' ')
