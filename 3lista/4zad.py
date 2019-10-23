mickiewicz = "Litwo! Ojczyzno moja! ty jesteś jak zdrowie: \
Ile cię trzeba cenić, ten tylko się dowie, \
Kto cię stracił. Dziś piękność twą w całej ozdobie \
Widzę i opisuję, bo tęsknię po tobie. \
Matka Boska, Opieka, CudPanno święta, co Jasnej bronisz Częstochowy \
I w Ostrej świecisz Bramie Ty, co gród zamkowy \
Nowogródzki ochraniasz z jego wiernym ludem! \
Jak mnie dziecko do zdrowia powróciłaś cudem \
(Gdy od płaczącej matki, pod Twoją opiekę \
Ofiarowany, martwą podniosłem powiekę; \
I zaraz mogłem pieszo, do Twych świątyń progu \
Iść za wrócone życie podziękować Bogu), \
Tak nas powrócisz cudem na Ojczyzny łono. \
RoślinyTymczasem przenoś moją duszę utęsknioną \
Do tych pagórków leśnych, do tych łąk zielonych, \
Szeroko nad błękitnym Niemnem rozciągnionych; \
Do tych pól malowanych zbożem rozmaitem, \
Wyzłacanych pszenicą, posrebrzanych żytem; \
Gdzie bursztynowy świerzop, gryka jak śnieg biała, \
Gdzie panieńskim rumieńcem dzięcielina pała, \
A wszystko przepasane jakby wstęgą, miedzą \
Zieloną, na niej z rzadka ciche grusze siedzą. \
DomŚród takich pól przed laty, nad brzegiem ruczaju, \
Na pagórku niewielkim, we brzozowym gaju, \
Stał dwór szlachecki, z drzewa, lecz podmurowany; \
DrzewoŚwieciły się z daleka pobielane ściany, \
Tym bielsze, że odbite od ciemnej zieleni \
Topoli, co go bronią od wiatrów jesieni. \
Dom mieszkalny niewielki, lecz zewsząd chędogi, \
I stodołę miał wielką, i przy niej trzy stogi \
Użątku, co pod strzechą zmieścić się nie może. \
Widać, że okolica obfita we zboże, \
I widać z liczby kopic, co wzdłuż i wszerz smugów \
Świecą gęsto jak gwiazdy, widać z liczby pługów \
Orzących wcześnie łany ogromne ugoru, \
Czarnoziemne, zapewne należne do dworu, \
Uprawne dobrze na kształt ogrodowych grządek: \
Że w tym domu dostatek mieszka i porządek. \
Brama na wciąż otwarta przechodniom ogłasza, \
Że gościnna, i wszystkich w gościnę zaprasza."

import random

def simplifySentence(text, wordLength, numberWords):
    wordsIn = text.split() 
    wordsOut = []
    for i in wordsIn:
        if len(i) < wordLength:
            wordsOut.append(i)
    while len(wordsOut) > numberWords:
        del wordsOut[random.randint(0, len(wordsOut)-1)]
    return ' '.join(wordsOut)

# print( len(mickiewicz) )
after = simplifySentence(mickiewicz, 10, 5)
print( after )
# print( len(after) )