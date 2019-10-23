import math

def squareRoot(n):
    for j in range(0,n+2):
        sum = 0
        for i in range(1,j+1):
            sum += (2*i-1)
        if sum > n:
            return j-1
    return 0


for i in range(0,100):
    if squareRoot(i) != math.floor(math.sqrt(i)):
        print("number: ", i, "\tsquareRoot: ", squareRoot(i), "\tmath: ", math.floor(math.sqrt(i)))