import timeit

def pierwsza_imperatywna(n):
    wynik = []
    for i in range(2,n+1):
        for j in range(2,i+1):
            if j==i:
                wynik.append(i)
            elif i%j == 0:
                break
    return wynik


def pierwsza_skladana(n):
    return [i for i in range(2,n+1) if len([j for j in range(2,i) if i%j == 0]) == 0 ]
    # return [x for x in range(2, n) if all(x % y != 0 for y in range(2, x))]

def pierwsza_funkcyjna(n):
    number_list = range(2, n+1)
    return list(filter(lambda x: len([j for j in range(2,x) if x%j == 0]) == 0, number_list))
    

print( pierwsza_imperatywna(20) )
print( pierwsza_skladana(20) )
print( pierwsza_funkcyjna(20) )

executions=10000
print( timeit.timeit('pierwsza_imperatywna(20)', setup="from __main__ import pierwsza_imperatywna", number=executions) )
print( timeit.timeit('pierwsza_skladana(20)', setup="from __main__ import pierwsza_skladana", number=executions) )
print( timeit.timeit('pierwsza_funkcyjna(20)', setup="from __main__ import pierwsza_funkcyjna", number=executions) )