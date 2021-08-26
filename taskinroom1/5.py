def storona(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        print ('Треугольник существует')
    else:
        print('Треугольник не существует')
a,b,c = map(int, input().split())        
storona(a,b,c)
