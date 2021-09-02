def findElement(pos, krat):
    for i in pos:
        if i%krat == 0:
            print(i)

a = [1,2,3,4,5,6]
findElement(a,3)
