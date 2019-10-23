import timeit

def rozklad_imperatywna(n):
    wynik = []
    for i in range(2,n+1):
        potega = 0
        while n%i == 0:
            potega += 1
            n /= i
        if potega != 0:
            wynik.append((i,potega))
    return wynik

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def rozklad_skladana(n):

    return [ (l,p) for l in range(2,n+1) for p in range(1,n+1) 
        if n%(l**p)==0 and n%(l**(p+1))!=0 and isPrime(l) ]

def rozklad_funkcyjna(n):
    return list( filter(lambda lp: n%(lp[0]**lp[1])==0 and n%(lp[0]**(lp[1]+1))!=0, 
        list((x,y) for x in filter(lambda x: n%x==0 and isPrime(x), range(2,n) ) for y in range(1,5) )))

print( rozklad_imperatywna(756) )
print( rozklad_skladana(756) )
print( rozklad_funkcyjna(756) )

executions=10000
print( timeit.timeit('rozklad_imperatywna(20)', setup="from __main__ import rozklad_imperatywna", number=executions) )
print( timeit.timeit('rozklad_skladana(20)', setup="from __main__ import rozklad_skladana", number=executions) )
print( timeit.timeit('rozklad_funkcyjna(20)', setup="from __main__ import rozklad_funkcyjna", number=executions) )