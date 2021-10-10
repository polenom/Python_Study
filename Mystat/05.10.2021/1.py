def FindDegree(x ,y):
    if y == 2:
        return x*x
    else:
        return x*(FindDegree(x,y-1))
print(FindDegree(int(input('Input number ')),int(input('Input degree '))))
