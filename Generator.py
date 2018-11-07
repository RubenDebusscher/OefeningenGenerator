#Importeer de libraries
from random import randint
#Maak de arrays aan
#alle mogelijke operaties
#alle mogelijke talstelsels
operaties =["+","-","*","/","AND","OR","XOR"]
mogelijke_talstelsels = ["10","16","8"]
oefeningen = []
aantal = 20

#maak een lus aan waarin je x aantal keer een random getal1 met signatuur, teken en randomgetal2 met signatuur
#TODO:geneste opgaves
count = 1
while (count <= aantal):
    #maak een array aan voor de oefeningen
    #maak arrays aan voor elke oefening
    #gebruik een randomiser om het aantal getallen te bepalen
    #plaats random aantal getallen erin met evenveel stelsels en 1 teken minder
    moeilijkheidsgraad = int(randint(2,4))
    elementen = 1
    oefening = []
    while (elementen <= moeilijkheidsgraad):
        oefening.append(randint(~500,500))
        oefening.append('('+ str(mogelijke_talstelsels[randint(0,2)])+')')
        oefening.append(operaties[randint(0,6)])
        elementen +=1
    oefening.pop()
    oefeningen.append(str(oefening))
    oefening.clear()
    
    count +=1

for item in oefeningen:
    list(item)
    print(item)

    #loop door de elementen waarbij per element word nagegaan of het een getal is, of een teken, indien teken, voer checks uit die omzetten en toevoegen aan de oplossing

    #maak een lus die kijkt of het element tussen haakjes staat, zo ja= zet element ervoor om in dat stelsel en append to string
    #in dezelfde lus, kijk of elk 3e element een teken is en voeg volgens deze de bewerking uit en plaats deze in een variabele
    #plaats oplossing aan het einde van de opgave
    #plaats alles in een html file

    #and = &
    #or = |
    #XOR = ^