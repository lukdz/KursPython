'''
http://www.ii.uni.wroc.pl/
'''
import re

adres = "([a-zA-Z]+\.)*[a-zA-Z]+"
automat = re.compile("http://" + adres)
with open('index.html', 'r') as fh:
    tekst = str(fh.read())

print( [ url.group() for url in automat.finditer(tekst) ] )

