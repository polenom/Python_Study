N = input()
a = N[:N.find('h')+1]
b = N[N.rfind('h'):]
c = N[N.rfind('h')-1:N.find('h'):-1]


print(a+c+b)
