class MyCountry():
    def __init__(self,country):
        self.country = country

    def addCountry(self, new):
        self.country +=(new,)

    def deleteCountry(self,mydel):
        self.country = tuple(i for i in self.country if i != mydel)

    def findCountry(self, slovo):
        for i in self.country:
            if slovo in i:
                return i
    def checkCountry(self, mycontry):
        return True if self.findCountry(mycontry) else False

a = ('ang','brazil', 'arg', 'bel')
x = MyCountry(a)
x.addCountry('vkl')
x.deleteCountry('arg')
print(x.country)
print(x.findCountry('be'))
print(x.checkCountry('vkl'))

