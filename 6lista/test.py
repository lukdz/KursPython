class IntIterator(object):
    def __init__ (self):
        self.licznik = 0
    def __next__ (self):
        wynik = self.licznik
        self.licznik += 1
        return wynik

class IntCollection(object):
    def __iter__ (self):
        return IntIterator()

suma = 0
for i in IntCollection():
    if suma + i >= 100: break
    suma += i

print( suma )