class electionResult:
    def __init__(self, name, party, votes):
        self.name = name
        self.votes = votes
        self.party = party
    def __lt__(self, other):
         return self.votes < other.votes

def calculateWinners(result, places):
    winners = []
    for i in range(1,places+1):
        for j in result:
            winners.append( (j.votes / i, j.party) )
    winners.sort(reverse=True, key=lambda x: x[0])
    winners = winners[1:places]
    winners = [x[1] for x in winners]
    dictionary = dict((i, winners.count(i)) for i in winners)
    return dictionary




result=[\
        electionResult("1Prawo", "Prawo i Sprawiedliwość",      8051935),\
        electionResult("2Prawo", "Prawo i Sprawiedliwość",      8051935),\
        electionResult("3Prawo", "Prawo i Sprawiedliwość",      8051935),\
        electionResult("4Prawo", "Prawo i Sprawiedliwość",      8051935),\
        electionResult("5Prawo", "Prawo i Sprawiedliwość",      8051935),\
        electionResult("1KKW", "KKW Koalicja Obywatelska PO .N iPL Zieloni",    5060355),\
        electionResult("2KKW", "KKW Koalicja Obywatelska PO .N iPL Zieloni",    5060355),\
        electionResult("3KKW", "KKW Koalicja Obywatelska PO .N iPL Zieloni",    5060355),\
        electionResult("4KKW", "KKW Koalicja Obywatelska PO .N iPL Zieloni",    5060355),\
        electionResult("5KKW", "KKW Koalicja Obywatelska PO .N iPL Zieloni",    5060355),\
        electionResult("1Sojusz", "Sojusz Lewicy Demokratycznej",       2319946),\
        electionResult("2Sojusz", "Sojusz Lewicy Demokratycznej",       2319946),\
        electionResult("3Sojusz", "Sojusz Lewicy Demokratycznej",       2319946),\
        electionResult("4Sojusz", "Sojusz Lewicy Demokratycznej",       2319946),\
        electionResult("5Sojusz", "Sojusz Lewicy Demokratycznej",       2319946),\
        electionResult("1Polskie", "Polskie Stronnictwo Ludowe",        1578523),\
        electionResult("2Polskie", "Polskie Stronnictwo Ludowe",        1578523),\
        electionResult("3Polskie", "Polskie Stronnictwo Ludowe",        1578523),\
        electionResult("4Polskie", "Polskie Stronnictwo Ludowe",        1578523),\
        electionResult("5Polskie", "Polskie Stronnictwo Ludowe",        1578523),\
        electionResult("1Konfederacja", "Konfederacja Wolność i Niepodległość", 1256953),\
        electionResult("2Konfederacja", "Konfederacja Wolność i Niepodległość", 1256953),\
        electionResult("3Konfederacja", "Konfederacja Wolność i Niepodległość", 1256953),\
        electionResult("4Konfederacja", "Konfederacja Wolność i Niepodległość", 1256953),\
        electionResult("5Konfederacja", "Konfederacja Wolność i Niepodległość", 1256953),\
        electionResult("1KWW", "KWW Mniejszość Niemiecka",      32094),\
        electionResult("2KWW", "KWW Mniejszość Niemiecka",      32094),\
        electionResult("3KWW", "KWW Mniejszość Niemiecka",      32094),\
        electionResult("4KWW", "KWW Mniejszość Niemiecka",      32094),\
        electionResult("5KWW", "KWW Mniejszość Niemiecka",      32094),\
        electionResult("1KWW", "KWW Koalicja Bezpartyjni i Samorządowcy",       144773),\
        electionResult("2KWW", "KWW Koalicja Bezpartyjni i Samorządowcy",       144773),\
        electionResult("3KWW", "KWW Koalicja Bezpartyjni i Samorządowcy",       144773),\
        electionResult("4KWW", "KWW Koalicja Bezpartyjni i Samorządowcy",       144773),\
        electionResult("5KWW", "KWW Koalicja Bezpartyjni i Samorządowcy",       144773),\
        electionResult("1Skuteczni", "Skuteczni Piotra Liroya-Marca",   18918),\
        electionResult("2Skuteczni", "Skuteczni Piotra Liroya-Marca",   18918),\
        electionResult("3Skuteczni", "Skuteczni Piotra Liroya-Marca",   18918),\
        electionResult("4Skuteczni", "Skuteczni Piotra Liroya-Marca",   18918),\
        electionResult("5Skuteczni", "Skuteczni Piotra Liroya-Marca",   18918),\
        electionResult("1Akcja", "Akcja Zawiedzionych Emerytów Rencistów",      5448),\
        electionResult("2Akcja", "Akcja Zawiedzionych Emerytów Rencistów",      5448),\
        electionResult("3Akcja", "Akcja Zawiedzionych Emerytów Rencistów",      5448),\
        electionResult("4Akcja", "Akcja Zawiedzionych Emerytów Rencistów",      5448),\
        electionResult("5Akcja", "Akcja Zawiedzionych Emerytów Rencistów",      5448),\
        electionResult("1Prawica", "Prawica ",  1765),\
        electionResult("2Prawica", "Prawica ",  1765),\
        electionResult("3Prawica", "Prawica ",  1765),\
        electionResult("4Prawica", "Prawica ",  1765),\
        electionResult("5Prawica", "Prawica ",  1765)]
wynik = calculateWinners(result,460)
for i in wynik:
    print(wynik[i], i)



# awk '{for (i = 1; i <= 5; ++i) printf "\telectionResult(\""i$1"\", \"" $0 "),\\\n"}' wyniki.txt