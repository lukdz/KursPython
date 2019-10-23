import timeit
from functools import reduce

def doskonale_imperatywna(n):
    wynik = []
    for i in range(2,n+1):
        suma = 0
        for j in range(1,i):
            if i%j == 0:
                suma += j
        if suma == i:
            wynik.append(i)
    return wynik

def doskonale_skladana(n):
    return [i for i in range(2,n+1) if sum([j for j in range(1,i) if i%j == 0]) == i ]

def doskonale_funkcyjna(n):
    return list(filter(lambda x: x==reduce(lambda a, b: a + b,(filter( lambda y: x%y==0, range(1, x)))), range(2,n+1)) )

number=1000
print( doskonale_imperatywna(number) )
print( doskonale_skladana(number) )
print( doskonale_funkcyjna(number) )

executions=10000
print( timeit.timeit('doskonale_imperatywna(20)', setup="from __main__ import doskonale_imperatywna", number=executions) )
print( timeit.timeit('doskonale_skladana(20)', setup="from __main__ import doskonale_skladana", number=executions) )
print( timeit.timeit('doskonale_funkcyjna(20)', setup="from __main__ import doskonale_funkcyjna", number=executions) )