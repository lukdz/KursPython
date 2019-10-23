import itertools

class Formula:
    def zmienne(self):
        pass
    def oblicz(self, dict):
        pass
    def tautologia(self):
        number_variable = len(self.zmienne())
        for i in range(number_variable + 1):
            value = [ x < i for x in range(number_variable)]
            for j in list(itertools.permutations(value)):
                dictOfWords = dict(zip(self.zmienne(), j))
                if not self.oblicz(dictOfWords):
                    return False
        return True

class And(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def oblicz(self, zmienne):
        return self.left.oblicz(zmienne) and self.right.oblicz(zmienne)
    def __str__(self):
        return str(self.left) + " ∧ " + str(self.right)
    def zmienne(self):
        return self.left.zmienne().union(self.right.zmienne())     

class Or(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def oblicz(self, zmienne):
        return self.left.oblicz(zmienne) or self.right.oblicz(zmienne)
    def __str__(self):
        return str(self.left) + " v " + str(self.right)
    def zmienne(self):
        return self.left.zmienne().union(self.right.zmienne())

class Impl(Formula):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def oblicz(self, zmienne):
        return ( not self.left.oblicz(zmienne) ) or \
               ( self.left.oblicz(zmienne) and self.right.oblicz(zmienne) )
    def __str__(self):
        return str(self.left) + " => " + "(" + str(self.right) + ")"
    def zmienne(self):
        return self.left.zmienne().union(self.right.zmienne())

class Zmienna(Formula):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return str(self.name)
    def oblicz(self, zmienne):
        return zmienne[self.name]
    def zmienne(self):
        return {self.name}
    def tautologia(self):
        return False

class Prawda(Formula):
    def __str__(self):
        return str(True)
    def oblicz(self, zmienne):
        return True
    def zmienne(self):
        return set()
    def tautologia(self):
        return True

class Falsz(Formula):
    def __str__(self):
        return str(False)
    def oblicz(self, zmienne):
        return False
    def zmienne(self):
        return set()
    def tautologia(self):
        return False

thisdict = {
  "y": True,
  "x": False
}
print( "\nImpl" )
print( Impl(Zmienna("x"), And(Zmienna("y"), Prawda())) )
print( Impl(Zmienna("x"), And(Zmienna("y"), Prawda())).oblicz(thisdict) )
print( "\nStala" )
print( Prawda().tautologia() )
print( Falsz().tautologia() )
print( Zmienna("x").tautologia() )
print( "\nAnd" )
print( And(Zmienna("y"), Zmienna("x")).tautologia() )
print( And(Zmienna("y"), Prawda()).tautologia() )
print( And(Prawda(), Prawda()).tautologia() )
print( "\nOr" )
print( Or(Zmienna("y"), Zmienna("x")).tautologia() )
print( Or(Zmienna("y"), Prawda()).tautologia() )
print( Or(Prawda(), Prawda()).tautologia() )

