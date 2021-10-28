class MyCountry():
    def __init__(self,country):
        self.country = country

    def addCountry(self, new,capital):
        self.country[new] = capital

    def deleteCountry(self,mydel):
        del self.country[mydel]

    def findCountry(self, slovo,sel):
        if sel == 'country':
            return self.country.get(slovo, None)
        elif sel == 'capital':
            for k,v in self.country.items():
                if v == slovo:
                    return k
    def checkCountry(self, mycontry,sel):
        return True if self.findCountry(mycontry,sel) else False

a = {'ang':'lon','brazil':'brazil', 'arg':'boun', 'bel':'minsk'}
x = MyCountry(a)
x.addCountry('vkl', 'vilna')
x.deleteCountry('ang')
print(x.country)
print(x.findCountry('bel', 'country'))
print(x.checkCountry('bel','country'))
