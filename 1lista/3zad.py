def romb(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end='')
        for j in range((2*i)+1):
            print("#",end='')
        for j in range(n-i):
            print(" ",end='')
        print()
    for j in range(2*n+1):
        print("#",end='')
    print()
    for i in range(n):
        for j in range(i+1):
            print(" ",end='')
        for j in range((2*(n-i))-1):
            print("#",end='')
        for j in range(i+1):
            print(" ",end='')
        print()

romb(4)