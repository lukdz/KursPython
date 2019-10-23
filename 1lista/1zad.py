def vat_faktura(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma * 1.23

def vat_paragon(lista):
    suma = 0
    for i in lista:
        suma = suma + (i * 1.23)
    return suma 

zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy))
print(vat_paragon(zakupy))
print(vat_faktura(zakupy) == vat_paragon(zakupy))
zakupy = range(100)
print(vat_faktura(zakupy))
print(vat_paragon(zakupy))
print(vat_faktura(zakupy) == vat_paragon(zakupy))