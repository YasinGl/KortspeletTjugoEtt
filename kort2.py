#Funktion för att visa en hand som en sträng.
def visa_hand(hand):
    kort = " : ".join(map(str, hand))  #Skapar en sträng av korten i handen med mellanslag emellan.
    return kort
