#Importeer de libraries
from random import randint


def strip_Last_Operation(s):
    if s.endswith(" XOR "): s = s.rstrip( "XOR ")
    if s.endswith(" AND "): s = s.rstrip(" AND ")
    if s.endswith(" OR "): s = s.rstrip(" OR ")
    if s.endswith(" + "): s = s.rstrip(" + ")
    if s.endswith(" - "): s = s.rstrip(" - ")
    if s.endswith(" * "): s = s.rstrip(" * ")
    if s.endswith(" / "): s = s.rstrip(" / ")
    return s
#Maak de arrays aan
#alle mogelijke operaties
#alle mogelijke talstelsels
operaties =["+","-","*","/","AND","OR","XOR"]
mogelijke_talstelsels = ["10","16","8"]
oefening = []
oefeningen = {}
oefeningenStrings={}
oefeningenOplossingen={}
aantal = 20
count = 1

#maak een lus aan waarin je x aantal keer een random getal1 met signatuur, teken en randomgetal2 met signatuur
while (count <= aantal):
    #maak een array aan voor de oefeningen
    #maak arrays aan voor elke oefening
    #gebruik een randomiser om het aantal getallen te bepalen
    #plaats random aantal getallen erin met evenveel stelsels en 1 teken minder
    moeilijkheidsgraad = int(randint(2,4))
    elementen = 1
    
    oefeningstring = ""
    while (elementen <= moeilijkheidsgraad):
        stelsel = mogelijke_talstelsels[randint(0,2)]
        operatie = operaties[randint(0,6)]
        if(stelsel=="8"):
            num= randint(~500,500)
            oefening.append(num)
            oefeningstring += str(format(num,'0o'))
        elif(stelsel=="16"):
            num= randint(~500,500)
            oefening.append(num)
            oefeningstring += str(format(num,'0X'))
        else:
            num= randint(~500,500)
            oefening.append(num)
            oefeningstring += str(num)
        oefening.append('('+ str(stelsel)+')')
        oefeningstring += '('+ str(stelsel)+')'
        oefening.append(operatie)
        oefeningstring += " "+(operatie)+" "
        elementen +=1
    oefening.pop()
    #print(oefening)
    ##!Dit werkt nog niet, kan dit nagekeken worden?
    #oefeningen[count] = oefening
    # op de plaats waar "1" staat moet de oplossing komen ?? 
    oefeningen[count] = {oefeningstring: "1"}
    #print(oefeningen[count])
    ##dit werkt wel weer
    oefeningstring = strip_Last_Operation(oefeningstring)
    oefeningenStrings[count] = oefeningstring
    ##loop door de oefening array om de berekening te maken
    oefening.clear()
    oefeningstring = ""
    
    count +=1
    #maak de lijst weer zodanig dat het een array van de elementen wordt
    #loop door de elementen waarbij per element word nagegaan of het een getal is, of een teken, indien teken, voer checks uit die omzetten en toevoegen aan de oplossing

    #maak een lus die kijkt of het element tussen haakjes staat, zo ja= zet element ervoor om in dat stelsel en append to string
    #in dezelfde lus, kijk of elk 3e element een teken is en voeg volgens deze de bewerking uit en plaats deze in een variabele
    #plaats oplossing aan het einde van de opgave
    #plaats alles in een html file

    #and = &
    #or = |
    #XOR = ^

    #gebruik een dictionary key=string versie,value = array(niet omgezet)
    
for item in oefeningenStrings:
    #print(oefeningen[item])
    print(oefeningenStrings[item])
print(oefeningen)