import itertools

def display(a,b,c):
    maxabc = max([len(str(a)), len(str(b)), len(str(c))])
    print( '%*s' % (maxabc+1,a) )
    print( '+%*s' % (maxabc,b) )
    print( '-' * (maxabc+1) ) 
    print( '%*s' % (maxabc+1,c) )
    print()

def solve(a,b,c):
    display(a,b,c)
    letters = set(a+b+c)
    for numbers in \
            list(itertools.permutations(range(0,10), len(letters))):
        dictionary = dict(zip(letters, numbers))
        na=0
        for l in a:
            na = na*10 + dictionary[l]
        nb=0
        for l in b:
            nb = nb*10 + dictionary[l]
        nc=0
        for l in c:
            nc = nc*10 + dictionary[l]
        if ((na + nb) == nc):
            print( dictionary )
            display(na,nb,nc)
            
solve('KTO', 'KOT', 'TOK')
solve('TRZY', 'TRZY', 'SZESC')
solve('KOGUT', 'KURA', 'JAJKO')
solve('LUK', 'LUK', 'KOLO')
solve('REBUS', 'I', 'SUDOKU')
solve('USA','USSR','PEACE')
solve('SEND','MORE','MONEY')
solve('ZERO','ZERO','JEDEN')
solve('KIOTO', 'OSAKA', 'TOKIO')
