import time

def sudan(n, x, y):
    if n == 0:
        return x+y
    if y == 0:
        return x
    return sudan(n-1, sudan(n,x,y-1), sudan(n,x,y-1)+y)

def sudanDict(n, x, y, memo):
    if n == 0:
        return x+y
    if y == 0:
        return x
    if (n,x,y) in memo:
        return memo[(n,x,y)]
    memo[(n,x,y)] = sudanDict(n-1, sudanDict(n,x,y-1,memo), sudanDict(n,x,y-1,memo)+y,memo)
    return memo[(n,x,y)]

tests =[ \
    (0,5,5),\
    (1,5,5),\
    (1,5,9),\
    (1,9,5),\
    (1,9,9),\
    (2,1,1),\
    (2,1,2),\
    (2,2,1),\
    (2,2,2),\
    (2,3,3) ]
print( "n x y\t sudan\ttime\t\txSpeed" )
for i in tests:
    startDict = time.time()
    print( i[0], i[1], i[2], '\t',sudanDict(i[0], i[1], i[2], dict()), end = '')
    endDict = time.time()
    print("\t%10.3e" %(endDict - startDict))
    start = time.time()
    print( i[0], i[1], i[2], '\t',sudan(*i), end = '')
    end = time.time()
    print("\t%10.3e" %(end - start), end = '')
    print( "\t", (end - start) / (endDict - startDict) )



