def reszta(kwota):
    ilosc_lista=[]
    monety=[1, 2, 5, 10, 20]
    monety.reverse()
    for i in monety:
        ilosc=0
        while kwota-i >= 0:
            ilosc+=1
            kwota-=i
        ilosc_lista.append(ilosc)
    monety.reverse()
    ilosc_lista.reverse()
    return (monety, ilosc_lista)

print(reszta(123))