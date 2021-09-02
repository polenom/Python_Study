def enum(spisok, n):
    return [ b for a,b in enumerate(spisok) if (a+1)%n == 0]

def ran(spisok, n):
    return [ spisok[a] for a in range(len(spisok)) if (a+1)%3 == 0]

print(enum([1,2,3,4,5,6,7], 3))
print(ran([1,2,3,4,5,6,7], 3))
