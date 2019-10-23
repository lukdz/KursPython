def rozklad(liczba):
    wynik=[]
    for i in range(2,liczba):
        ilosc=0
        while liczba % i == 0:
            liczba/=i
            ilosc+=1
        if ilosc != 0:
            wynik.append((i, ilosc))
    return wynik

print(rozklad(756))