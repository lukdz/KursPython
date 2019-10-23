def tabliczka(y_min, y_max, x_min, x_max):
    i=len(str(y_max*x_max))+2
    format = '%' + ("%i" % i)
    print((format + 's') % (''),end='')
    for y in range(y_min, y_max+1):
        print((format + 'd') % (y),end='')
    print()
    for x in range(x_min, x_max+1):
        print((format + 'd') % (x),end='')
        for y in range(y_min, y_max+1):
            print((format + 'd') % (x*y),end='')
        print()

tabliczka(3, 5, 2, 4)
tabliczka(807, 809, 907, 909)