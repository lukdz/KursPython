import timeit
from functools import reduce

def zaprzyjaznione_imperatywna(n):
    solution = []
    for i in range(2,n+1):
        sumai = 0
        sumaj = 0
        for j in range(1,i):
            if i%j == 0:
                sumai += j
        for j in range(1,sumai):
            if sumai%j == 0:
                sumaj += j
        if i == sumaj and sumai != sumaj and sumai > sumaj:
            solution.append((i,sumai))
    return solution

def zaprzyjaznione_skladana(n):
    return [
        x for x in
        [(i,sum([j for j in range(1,i) if i%j==0])) for i in range(2,n+1)]
        if x[0]<x[1] and x[0]==sum([j for j in range(1,x[1]) if x[1]%j==0])
    ]

def zaprzyjaznione_funkcyjna(n):
    return list( 
        filter(lambda z: z[0]==reduce(lambda a, b: a + b,(filter(lambda d: z[1]%d==0, range(1,z[1])))), 
        filter(lambda y: y[0]<y[1], 
        map(lambda x: (x,reduce(lambda a, b: a + b,(filter(lambda d: x%d==0, range(1,x))),0)), 
        range(1,n+1) )))
    )

print( zaprzyjaznione_imperatywna(1300) )
print( zaprzyjaznione_skladana(1300) )
print( zaprzyjaznione_funkcyjna(1300) )

executions=10000
print( timeit.timeit('zaprzyjaznione_imperatywna(20)', setup="from __main__ import zaprzyjaznione_imperatywna", number=executions) )
print( timeit.timeit('zaprzyjaznione_skladana(20)', setup="from __main__ import zaprzyjaznione_skladana", number=executions) )
print( timeit.timeit('zaprzyjaznione_funkcyjna(20)', setup="from __main__ import zaprzyjaznione_funkcyjna", number=executions) )