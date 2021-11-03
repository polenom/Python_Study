def comp(a: dict,b: dict):
    res = [[],[]]
    for k,v in a.items():
        if b.get(k, False):
            res[ 0 if v==b[k] else 1 ].append(k)
    return res
class Duck:
    def __init__(self, color: str, old: int ,fly: bool = False, swim: bool = False, cra: bool = False):
        print('Утка родилась')
        self.color = color
        self.old = old
        self.fly = fly
        self.swim = swim
        self.cra = cra

    def getduck(self):
        return self.__dict__


class Toy:
    def __init__(self,color: str, old: int, country: str, cost: float,fly: bool = False, swim: bool = False, cra: bool = False):
        print('Утка родилась')
        self.color = color
        self.old = old
        self.cost = cost
        self.country = country
        self.fly = fly
        self.swim = swim
        self.cra = cra

    def getduck(self):
        return self.__dict__

class WildDuck(Duck):
    def __init__(self, color: str, old: int, fly: bool = True, swim: bool = True, cra: bool = True):
        super().__init__(color,old,fly,swim,cra)

class RedHeadedDuck(Duck):
    def __init__(self,color: str, old: int , fly: bool = True, swim: bool = True, cra: bool = True):
        super().__init__(color,old,fly,swim,cra)

class DecoyDuck(Duck):
    def __init__(self,color: str, old: int , swim: bool = True):
        super().__init__(color,old,swim=swim)

class RubberDuck(Toy):
    def __init__(self,*args):
        super().__init__(*args,cra=True,swim=True)


class ToyDuck(Toy):
    def __init__(self,*args):
        super().__init__(*args,fly=True)

import threading
import time
def sea():
    global x
    a1 = id(x)
    while a1 == id(x):
        time.sleep(1)
        x =33
    print('Утка умерла')
x = ToyDuck(1,2,3,4)
ch = threading.Thread(target=sea).start()

time.sleep(5)
x = 1
time.sleep(5)
