import random

def rakna_poang(hand):
    poang = sum(hand)
    if 11 in hand and poang > 21:
        hand.remove(11)
        hand.append(1)
    return  poang
def räkna_poang(hand):
    poang = sum(hand)
    if 11 in hand and poang > 21:
        hand.remove(11)
        hand.append(1)
    return poang

# test