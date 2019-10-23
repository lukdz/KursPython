#zaszyfruj(tekst, cz)
def zaszyfruj(tekst, klucz):
    return ''.join(chr(ord(c)^klucz) for c in tekst)

def odszyfruj(szyfr, klucz):
    return zaszyfruj(szyfr, klucz)

klucz=7
print(zaszyfruj("Python", klucz))
print(odszyfruj(zaszyfruj("Python", klucz), klucz))