import random  #Importera random-modulen för att blanda kortleken.
from rakna import *
from kort2 import *

#Huvudfunktionen som implementerar spelet "Tjugoett" (Blackjack).
def tjugoett():
    print("Välkommen till Tjugoett!")
    print("Vi önskar dig stort lycka till, du kommer behöva det!")
    kor = input("Starta spel? Ja/Nej?: ").lower()  #Fråga spelaren om de vill starta spelet och omvandla svaret till små bokstäver.

    if kor == "ja":  # Om spelaren svarar "ja":
        kortlek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 14] * 4  # Skapa en kortlek med värden och antal kopior.
        random.shuffle(kortlek)  #Blanda kortleken slumpmässigt.

        spelare_hand = []  #Skapa en tom lista för spelarens hand.
        dealer_hand = []   #Skapa en tom lista för dealerns hand.

        #Dela ut två kort till spelaren och två kort till dealern.
        for dela in range(2):
            spelare_hand.append(kortlek.pop())
            dealer_hand.append(kortlek.pop())

        while True:
            print(f"Din hand: {visa_hand(spelare_hand)}, Poäng: {räkna_poang(spelare_hand)}")
            print(f"Dealerns hand: {dealer_hand[0]} _")

            val = input("Vill du dra ett kort? (J/N): ").lower()  #Fråga spelaren om de vill dra ett kort och omvandla svaret till små bokstäver.

            if val == "j":  #Om spelaren svarar "ja":
                spelare_hand.append(kortlek.pop())  # Dra ett kort från kortleken och lägg till i spelarens hand.
                if räkna_poang(spelare_hand) > 21:  # Om spelaren får över 21 poäng:
                    print(f"Din hand: {visa_hand(spelare_hand)}, Poäng: {räkna_poang(spelare_hand)}")
                    print("Du har över 21 poäng. Du förlorar.")
                    break  #Bryt loopen och avsluta spelet.

            else:
                break  #Om spelaren inte vill dra mer kort, bryt loopen och gå vidare.

        #Dealerns tur att dra kort (automatiserad regel att dra till 17 poäng eller mer).
        while räkna_poang(dealer_hand) < 17:
            dealer_hand.append(kortlek.pop())

        #Visa spelarens och dealerns händer samt jämför resultaten för att avgöra vinnaren.
        print(f"Din hand: {visa_hand(spelare_hand)}, Poäng: {räkna_poang(spelare_hand)}")
        print(f"Dealerns hand: {visa_hand(dealer_hand)}, Poäng: {räkna_poang(dealer_hand)}")

        if räkna_poang(spelare_hand) > 21:
            print("Dealern vinner. Du har över 21 poäng. (BUST)")
        elif räkna_poang(dealer_hand) > 21 or räkna_poang(spelare_hand) > räkna_poang(dealer_hand):
            print("Grattis! Du vinner! Hur gjorde du detta?")
        elif räkna_poang(spelare_hand) == räkna_poang(dealer_hand):
            print("Huset vinner tyvärr! Lycka till nästa gång.")
        else:
            print("Dealern vinner. Du kanske borde prova ett annat spel?")
    else:
        print("Vänligen svara JA/NEJ!?")
        tjugoett()  #  Om spelaren inte svarar "ja" eller "nej", starta om spelet.

tjugoett()  #Kör spelet när programmet körs.
