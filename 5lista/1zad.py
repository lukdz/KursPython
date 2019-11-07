import timeit
import time
import functools

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

def pierwsza_funkcyjna(n):
    number_list = range(2, n+1)
    return list(filter(lambda x: len([j for j in range(2,x) if x%j == 0]) == 0, number_list))

def pierwsza_yield(n):
    for i in range(2,n+1):
        for j in range(2,i+1):
            if j==i:
                yield i
            elif i%j == 0:
                break

print( '\t| imperatywna | funkcyjna | skladana | iterator')
for i in [10,100,1000]:
    print( '%7d' % i, end=' ')
    executions=100
    print( '|%12.3f' % timeit.Timer(functools.partial(pierwsza_imperatywna,i)).timeit(5), end=' ' )
    print( '|%10.3f' % timeit.Timer(functools.partial(pierwsza_skladana,i)).timeit(5), end=' ' )
    print( '|%9.3f' % timeit.Timer(functools.partial(pierwsza_funkcyjna,i)).timeit(5), end=' ' )

    start_time = time.time()  
    sum=0
    for i in pierwsza_yield(i):
        sum+=i
    print( '|%9.3f' % (time.time() - start_time), end=' ')

    print()
