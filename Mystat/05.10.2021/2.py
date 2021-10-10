def InputNumbers(a,b):
    if a+1 == b:
        return a+b
    else:
        return a+(InputNumbers(a+1,b))
print(InputNumbers(int(input('Input first number = ')),int(input('Input last number = '))))

