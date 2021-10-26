

class Equation():
    def __init__(self,equ:str):
        import re
        equ=equ.replace(' ', '')
        equ = [i for i in re.findall('\d*|[=]|x\^\d|x|[+-]', equ) if i]
        equ1 = []
        for num,i in enumerate(equ):
            if i == '0':
                equ1.append(i)
            elif  i.isdigit() and num == 0:
                equ1.append('+')
                equ1.append(i)
            elif  i.isdigit() and equ[num-1] == '=':
                equ1.append('+')
                equ1.append(i)
            elif i.isdigit():
                equ1.append('-' if equ[num-1] in ['-'] else '+')
                equ1.append(i)
            elif i == '=':
                equ1.append(i)
            elif 'x' in i and num == 0:
                equ1+=['+','1',i]
            elif 'x' in i and equ[num-1].isdigit():
                equ1.append(i)
            elif 'x' in i :
                equ1.append('-' if equ[num-1] in ['-'] else '+')
                equ1+=['1',i]

        if equ1[0] == '0':
            equ= equ1[2:]+['=','0']
        else:
            equ = []
            for num, i in enumerate(equ1):
                if num> equ1.index('=') and i in ['-','+']:
                    equ.append('+' if i == '-' else '-')
                elif i == '=':
                    pass
                elif i == '0':
                    equ.append('=')
                    equ.append('0')
                    break
                else:
                    equ.append(i)
            else:
                equ.append('=')
                equ.append('0')
        self.equ = equ
    pass
    # def solve(self):

class LinearEquation(Equation):
    def __init__(self,equ:str):
        import re
        Equation.__init__(self,equ)
        self.a = int(re.search('[\-\+]\d+x\^1', ''.join(self.equ))[0][:-3]) if 'x^1'in self.equ else int(re.search('[\-\+]\d+x[^\^]', ''.join(self.equ))[0][:-2])
        self.b = int(re.search('[\-\+]\d+[^x]',''.join(self.equ))[0][:-1]) if re.search('[\-\+]\d+[^x]',''.join(self.equ)) else 0
    def solve(self):
        return (-1*self.b)/self.a

class QuadraticEquation(Equation):
    def __init__(self,equ):
        import re
        Equation.__init__(self, equ)
        self.a = int(re.search('[\-\+]\d+x\^2',''.join(self.equ))[0][:-3])
        self.b = int(re.search('[\-\+]\d+x\^1', ''.join(self.equ))[0][:-3]) if 'x^1'in self.equ else int(re.search('[\-\+]\d+x[^\^]', ''.join(self.equ))[0][:-2])
        self.c = int(re.search('[\-\+]\d+[^x]',''.join(self.equ))[0][:-1]) if re.search('[\-\+]\d+[^x]',''.join(self.equ)) else 0

    def solve(self):
        D = (self.b**2-4*self.a*self.b)**0.5
        if D == 0:
            return ((-1*self.b)/(2*self.a))
        else:
            return ((-1*self.b+D)/2*self.a,(-1*self.b-D)/2*self.a)

z = QuadraticEquation(input('Input equation (example 2x^2+3^x+15=0): '))
print(z.solve())
