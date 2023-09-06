#Funktion för att räkna poäng i en hand.
def räkna_poang(hand):
    poang = sum(hand)  #Beräkna totala poängen i handen genom att summera värdena på korten.
    if 14 in hand and poang > 21:  # Om det finns ett kort med värde 14 i handen och totalpoängen är över 21:
        hand.remove(14)  #Ta bort kortet med värde 14 från handen.
        hand.append(1)   #Lägg till ett kort med värde 1 istället.
    return poang  #Returnera den beräknade poängen.