class Wyrazenie:
    def test(self):
        return

class Stala(Wyrazenie):
    def __init__(self, value):
        self.value = value
    def oblicz(self, zmienne):
        return self.value
    def wykonaj(self, zmienne):
        return self.value
    def __str__(self):
        return str(self.value)

class BrakWartosci(Exception):
   def __str__(self):
       return "BrakWartosci Exception"

class Zmienna(Wyrazenie):
    def __init__(self, name):
        self.name = name
    def oblicz(self, zmienne):
        try:
            wynik = zmienne[self.name]
        except KeyError:
            raise BrakWartosci
        return wynik
    def wykonaj(self, zmienne):
        return self.oblicz(zmienne)
    def __str__(self):
        return str(self.name)

class Przypisz(Wyrazenie):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def wykonaj(self, zmienne):
        try:
            zmienne[self.name]
        except KeyError:
            raise BrakWartosci
        zmienne[self.name] = self.value.wykonaj(zmienne)
        return zmienne
    def __str__(self):
        return str(self.name) + " = " + str(self.value)

class Warunkowo(Wyrazenie):
    def __init__(self, warunek, cialo):
        self.warunek = warunek
        self.cialo = cialo
    def wykonaj(self, zmienne):
        if self.warunek.wykonaj(zmienne):
            self.cialo.wykonaj(zmienne)
        return zmienne
    def __str__(self):
        return "if " + str(self.warunek) + "\nthen " + str(self.cialo)

class Petla(Wyrazenie):
    def __init__(self, warunek, cialo):
        self.warunek = warunek
        self.cialo = cialo
    def wykonaj(self, zmienne):
        while self.warunek.wykonaj(zmienne):
            self.cialo.wykonaj(zmienne)
        return zmienne
    def __str__(self):
        return "When " + str(self.warunek) + "\nthen " + str(self.cialo)

class Dodaj(Wyrazenie):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    def oblicz(self, zmienne):
        return self.left.oblicz(zmienne) + self.right.oblicz(zmienne)
    def __str__(self):
        return "(" + str(self.left) + "+" + str(self.right) + ")"

class Odejmij(Wyrazenie):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    def oblicz(self, zmienne):
        return self.left.oblicz(zmienne) - self.right.oblicz(zmienne)
    def __str__(self):
        return "(" + str(self.left) + "-" + str(self.right) + ")"

class Razy(Wyrazenie):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    def oblicz(self, zmienne):
        return self.left.oblicz(zmienne) * self.right.oblicz(zmienne)
    def __str__(self):
        return "(" + str(self.left) + "*" + str(self.right) + ")"

class DzielZero(Exception):
   def __str__(self):
       return "DzielZero Exception"

class Podziel(Wyrazenie):
    def __init__(self, left, right):
        self.left = left 
        self.right = right
    def oblicz(self, zmienne):
        if self.right.oblicz(zmienne) == 0:
            raise DzielZero
        return self.left.oblicz(zmienne) / self.right.oblicz(zmienne)
    def __str__(self):
        return "(" + str(self.left) + "/" + str(self.right) + ")"

print( Stala(5) )
thisdict = {
  "y": 0,
  "x": 1
}
print( Zmienna("y") )
print( Zmienna("y").oblicz(thisdict) )
print( Dodaj(Zmienna("x"), Stala(5)) )
print( Dodaj(Zmienna("x"), Stala(5)).oblicz(thisdict) )
print( Podziel(Zmienna("x"), Stala(0)) )
try:
    print( Podziel(Zmienna("x"), Stala(0)).oblicz(thisdict) )
except DzielZero as x:
    print(x)
try:
    print( Zmienna("z").oblicz(thisdict) )
except BrakWartosci as x:
    print(x)
print( "\nPRZYPISZ")
print( Zmienna("y").oblicz(thisdict))
print( Przypisz("y",Stala(2)).wykonaj(thisdict.copy()))
print( "\nIF")
print( Warunkowo(Zmienna("x"),Przypisz("y",Stala(2))) )
print( Warunkowo(Zmienna("x"),Przypisz("y",Stala(2))).wykonaj(thisdict.copy()))
print( Warunkowo(Zmienna("y"),Przypisz("y",Stala(2))).wykonaj(thisdict.copy()))
print( "\nWHEN")
print( Petla(Zmienna("x"),Przypisz("y",Stala(2))) )
print( Petla(Zmienna("x"),Przypisz("x",Stala(0))).wykonaj(thisdict.copy()))
print( Petla(Zmienna("y"),Przypisz("y",Stala(2))).wykonaj(thisdict.copy()))