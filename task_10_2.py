# не доделал
import copy

class Clothes:
    All = []
    def __init__(self,name = None):
        self.name = name
        Clothes.All.append(self)

class Coat(Clothes):
    def __init__(self, V):
        self.V = V/6.5 + 0.5
        super().__init__("Coat")

    #@property
    #def V(self):
    #    return self.__V

    def FabricCalc(self,amount):
        return self.V * amount

class Costume(Clothes):
    def __init__(self, H):
        self.H = 2/H + 0.3

    @property
    def H(self):
        return self.H

    def FabricCalc(self, amount):
        return self.H*amount

t1 = Coat(3)
w2 = Costume(5)

