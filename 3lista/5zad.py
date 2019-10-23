def compression (text):
    output = ""
    lastLetter = ''
    counter = 0
    for i in text+" ":
        if i == lastLetter:
            counter += 1
        else:
            if counter != 0:
                output += str(counter+1) + lastLetter
                counter = 0
            else:
                output += lastLetter
        lastLetter = i
    return output

def decompression (text):
    output = ""
    lastLetter = ''
    counter = 0
    for i in text+" ":
        if '0' <= i <= '9':
            counter *= 10
            counter += int(i)
            output += lastLetter
        else:
            if counter != 0:
                output += i*(counter-1)
                counter = 0
            else:
                output += lastLetter
        lastLetter = i
    return output

print( compression("aaaaa") )
print( compression("suuuuper") )
print( decompression("s4uper") )