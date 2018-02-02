'''
Project Euler Problem 54:

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players have
a pair of queens, then highest cards in each hand are compared (see example 4
below); if the highest cards tie then the next highest cards are compared,
and so on.

Consider the following five hands dealt to two players:



Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD          2C 3S 8S 8D TD          Player 2
                Pair of Fives           Pair of Eights

2	 	5D 8C 9S JS AC          2C 5C 7D 8S QH          Player 1
                Highest card Ace        Highest card Queen      
 	
3	 	2D 9C AS AH AC          3D 6D 7D TD QD          Player 2
                Three Aces              Flush with Diamonds     
 	
4	 	4D 6S 9H QH QC          3D 6D 7H QD QS          Player 1
                Pair of Queens          Pair of Queens
                Highest card Nine       Highest card Seven
 	
5	 	2H 2D 4C 4D 4S          3C 3D 3S 9S 9D          Player 1
                Full House              Full House
                With Three Fours        With Three Threes
 	
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
'''

#implement a card value ranker
#implement a hand evaluator for rank
#implement a tie breaker -- dependent on rank?
#readlines
#compare hands line at a time

import collections

card_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
hand_rank = ["HC", "1P", "2P", "3K", "ST", "FL", "FH", "4K", "SF", "RF"]

class card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return(self.value + self.suit)

    def __repr__(self):
        return self.__str__()

    def compare(self, other_card):
        #if this card wins, we return higher; if it loses, we return lower
        #if it's a tie, we return tie
        global card_rank
        this_rank = card_rank.index(self.value)
        other_rank = card_rank.index(other_card.value)
        if this_rank < other_rank:
            return "lower"
        elif other_rank < this_rank:
            return "higher"
        else:
            return "tie"

def is_royal_flush(cards):
    if is_straight_flush(cards):
        values = ["A", "K", "Q", "J", "T"]
        for card in cards:
            try:
                values.remove(card.value)
            except ValueError:
                return False
        return True
    return False

def is_straight_flush(cards):
    if is_flush(cards):
        if is_straight(cards):
            return True
    return False

def is_four_of_a_kind(cards):
    values = [card.value for card in cards]
    counter = collections.Counter(values)
    if counter.most_common()[0][1] == 4:
        return True
    return False

def is_full_house(cards):
    values = [card.value for card in cards]
    counter = collections.Counter(values)
    if is_three_of_a_kind(cards):
        if counter.most_common()[1][1] == 2:
            return True
    return False

def is_flush(cards):
    suits = set([card.suit for card in cards])
    if len(suits) > 1:
        return False
    return True

def is_straight(cards):
    global card_rank
    values = [card.value for card in cards]
    starting_index = card_rank.index(values[0])
    if values == card_rank[starting_index : starting_index+5]:
        return True
    return False

def is_three_of_a_kind(cards):
    values = [card.value for card in cards]
    counter = collections.Counter(values)
    if counter.most_common()[0][1] == 3:
        return True
    return False

def is_two_pair(cards):
    values = [card.value for card in cards]
    counter = collections.Counter(values)
    if is_one_pair(cards):
        if counter.most_common()[1][1] == 2:
            return True
    return False

def is_one_pair(cards):
    values = [card.value for card in cards]
    counter = collections.Counter(values)
    if counter.most_common()[0][1] == 2:
        return True
    return False

def tie_breaker(hand, other_hand):
    rank = hand.rank
    winner = None
    if rank == "RF":
        print("Impossible, via the problem statement.")
    elif rank == "SF":
        winner = tie_breaker_sf(hand, other_hand)
    elif rank == "4K":
        winner = tie_breaker_4k(hand, other_hand)
    elif rank == "FH":
        winner = tie_breaker_fh(hand, other_hand)
    elif rank == "FL":
        winner = tie_breaker_fl(hand, other_hand)
    elif rank == "ST":
        winner = tie_breaker_st(hand, other_hand)
    elif rank == "3K":
        winner = tie_breaker_3k(hand, other_hand)
    elif rank == "2P":
        winner = tie_breaker_2p(hand, other_hand)
    elif rank == "1P":
        winner = tie_breaker_1p(hand, other_hand)
    elif rank == "HC":
        winner = tie_breaker_hc(hand, other_hand)
    return winner

def tie_breaker_sf(hand, other_hand):
    #compare highest cards - know they are different by problem statement
    return hand.cards[-1].compare(other_hand.cards[-1])

def tie_breaker_4k(hand, other_hand):
    #compare four-of-a-kinds; if they match, compare other card
    global card_rank
    hand_vals = [card.value for card in hand.cards]
    other_hand_vals = [card.value for card in other_hand.cards]
    hand_count = collections.Counter(hand_vals)
    other_hand_count = collections.Counter(other_hand_vals)
    hand_kind = None
    hand_kicker = None
    for item in hand_count:
        if hand_count[item] == 4:
            hand_kind = item
        if hand_count[item] == 1:
            hand_kicker = item
    other_hand_kind = None
    other_hand_kicker = None
    for item in other_hand_count:
        if other_hand_count[item] == 4:
            other_hand_kind = item
        if other_hand_count[item] == 1:
            other_hand_kicker = item
    if card_rank.index(hand_kind) > card_rank.index(other_hand_kind):
        return "higher"
    elif card_rank.index(hand_kind) < card_rank.index(other_hand_kind):
        return "lower"
    else:
        if card_rank.index(hand_kicker) > card_rank.index(other_hand_kicker):
            return "higher"
        elif card_rank.index(hand_kicker) < card_rank.index(other_hand_kicker):
            return "lower"
        else:
            print("Impossible, via the problem statement.")

def tie_breaker_fh(hand, other_hand):
    #compare three-of-a-kinds; if they match, compare pair
    global card_rank
    hand_vals = [card.value for card in hand.cards]
    other_hand_vals = [card.value for card in other_hand.cards]
    hand_count = collections.Counter(hand_vals)
    other_hand_count = collections.Counter(other_hand_vals)
    hand_3k = None
    hand_1p = None
    for item in hand_count:
        if hand_count[item] == 3:
            hand_3k = item
        if hand_count[item] == 2:
            hand_1p = item
    other_hand_3k = None
    other_hand_1p = None
    for item in other_hand_count:
        if other_hand_count[item] == 3:
            other_hand_3k = item
        if other_hand_count[item] == 2:
            other_hand_1p = item
    if card_rank.index(hand_3k) > card_rank.index(other_hand_3k):
        return "higher"
    elif card_rank.index(hand_3k) < card_rank.index(other_hand_3k):
        return "lower"
    else:
        if card_rank.index(hand_1p) > card_rank.index(other_hand_1p):
            return "higher"
        elif card_rank.index(hand_1p) < card_rank.index(other_hand_1p):
            return "lower"
        else:
            print("Impossible, via the problem statement.")

def tie_breaker_fl(hand, other_hand):
    #compare cards from the end of each hand until we find a victor
    cards = hand.cards
    other_cards = other_hand.cards
    while True:
        card = cards.pop()
        other_card = other_cards.pop()
        if card.compare(other_card) != "tie":
            return card.compare(other_card)
        
def tie_breaker_st(hand, other_hand):
    #compare highest cards - know they are different by problem statement
    return hand.cards[-1].compare(other_hand.cards[-1])

def tie_breaker_3k(hand, other_hand):
    #compare three-of-a-kinds; if they match, compare kicker then 2nd kicker
    global card_rank
    hand_vals = [card.value for card in hand.cards]
    other_hand_vals = [card.value for card in other_hand.cards]
    hand_count = collections.Counter(hand_vals)
    other_hand_count = collections.Counter(other_hand_vals)
    hand_3k = None
    hand_kickers = []
    for item in hand_count:
        if hand_count[item] == 3:
            hand_3k = item
        if hand_count[item] == 1:
            hand_kickers.append(item)
    other_hand_3k = None
    other_hand_kickers = []
    for item in other_hand_count:
        if other_hand_count[item] == 3:
            other_hand_3k = item
        if other_hand_count[item] == 1:
            other_hand_kickers.append(item)
    if card_rank.index(hand_3k) > card_rank.index(other_hand_3k):
        return "higher"
    elif card_rank.index(hand_3k) < card_rank.index(other_hand_3k):
        return "lower"
    else:
        hand_kickers.sort(key = lambda x: card_rank.index(x))
        other_hand_kickers.sort(key = lambda x: card_rank.index(x))
        hand_kicker = hand_kickers.pop()
        other_hand_kicker = other_hand_kickers.pop()
        if card_rank.index(hand_kicker) > card_rank.index(other_hand_kicker):
            return "higher"
        elif card_rank.index(hand_kicker) < card_rank.index(other_hand_kicker):
            return "lower"
        else:
            hand_kicker2 = hand_kickers.pop()
            other_hand_kicker2 = other_hand_kickers.pop()
            if card_rank.index(hand_kicker2) > \
               card_rank.index(other_hand_kicker2):
                return "higher"
            elif card_rank.index(hand_kicker2) > \
                 card_rank.index(other_hand_kicker2):
                return "lower"
            else:
                print("Impossible, via the problem statement.")

def tie_breaker_2p(hand, other_hand):
    #compare top pair, compare second pair, compare kicker
    global card_rank
    hand_vals = [card.value for card in hand.cards]
    other_hand_vals = [card.value for card in other_hand.cards]
    hand_count = collections.Counter(hand_vals)
    other_hand_count = collections.Counter(other_hand_vals)
    hand_pairs = []
    hand_kicker = None
    for item in hand_count:
        if hand_count[item] == 2:
            hand_pairs.append(item)
        elif hand_count[item] == 1:
            hand_kicker = item
    other_hand_pairs = []
    other_hand_kicker = None
    for item in other_hand_count:
        if other_hand_count[item] == 2:
            other_hand_pairs.append(item)
        elif other_hand_count[item] == 1:
            other_hand_kicker = item
    hand_pairs.sort(key = lambda x: card_rank.index(x))
    other_hand_pairs.sort(key = lambda x: card_rank.index(x))
    hand_top = hand_pairs.pop()
    other_hand_top = other_hand_pairs.pop()
    if card_rank.index(hand_top) > card_rank.index(other_hand_top):
        return "higher"
    elif card_rank.index(hand_top) < card_rank.index(other_hand_top):
        return "lower"
    else:
        hand_second = hand_pairs.pop()
        other_hand_second = other_hand_pairs.pop()
        if card_rank.index(hand_second) > card_rank.index(other_hand_second):
            return "higher"
        elif card_rank.index(hand_second) < card_rank.index(other_hand_second):
            return "lower"
        else:
            if card_rank.index(hand_kicker) > \
               card_rank.index(other_hand_kicker):
                return "higher"
            elif card_rank.index(hand_kicker) < \
                 card_rank.index(other_hand_kicker):
                return "lower"
            else:
                print("Impossible, via the problem statement.")

def tie_breaker_1p(hand, other_hand):
    #compare pair, compare kickers
    global card_rank
    hand_vals = [card.value for card in hand.cards]
    other_hand_vals = [card.value for card in other_hand.cards]
    hand_count = collections.Counter(hand_vals)
    other_hand_count = collections.Counter(other_hand_vals)
    hand_pair = None
    hand_kickers = []
    for item in hand_count:
        if hand_count[item] == 2:
            hand_pair = item
        elif hand_count[item] == 1:
            hand_kickers.append(item)
    other_hand_pair = None
    other_hand_kickers = []
    for item in other_hand_count:
        if other_hand_count[item] == 2:
            other_hand_pair = item
        elif other_hand_count[item] == 1:
            other_hand_kickers.append(item)
    if card_rank.index(hand_pair) > card_rank.index(other_hand_pair):
        return "higher"
    elif card_rank.index(hand_pair) < card_rank.index(other_hand_pair):
        return "lower"
    else:
        hand_kickers.sort(key = lambda x: card_rank.index(x))
        other_hand_kickers.sort(key = lambda x: card_rank.index(x))
        for i in range(len(hand_kickers)):
            hand_kicker = hand_kickers.pop()
            other_hand_kicker = other_hand_kickers.pop()
            if card_rank.index(hand_kicker) > \
               card_rank.index(other_hand_kicker):
                return "higher"
            elif card_rank.index(hand_kicker) < \
                 card_rank.index(other_hand_kicker):
                return "lower"

def tie_breaker_hc(hand, other_hand):
    global card_rank
    hand_vals = [card.value for card in hand.cards]
    other_hand_vals = [card.value for card in other_hand.cards]
    hand_vals.sort(key = lambda x: card_rank.index(x))
    other_hand_vals.sort(key = lambda x: card_rank.index(x))
    for i in range(len(hand_vals)):
        hand_kicker = hand_vals.pop()
        other_hand_kicker = other_hand_vals.pop()
        if card_rank.index(hand_kicker) > \
               card_rank.index(other_hand_kicker):
            return "higher"
        elif card_rank.index(hand_kicker) < \
                 card_rank.index(other_hand_kicker):
            return "lower"

class hand():

    def __init__(self, cards):
        global card_rank
        self.cards = cards
        self.cards.sort(key = lambda card: card_rank.index(card.value))
        self.rank = self.get_rank()

    def __repr__(self):
        return(str([card for card in self.cards]))

    def get_rank(self):
        if is_royal_flush(self.cards):
            return "RF"
        if is_straight_flush(self.cards):
            return "SF"
        if is_four_of_a_kind(self.cards):
            return "4K"
        if is_full_house(self.cards):
            return "FH"
        if is_flush(self.cards):
            return "FL"
        if is_straight(self.cards):
            return "ST"
        if is_three_of_a_kind(self.cards):
            return "3K"
        if is_two_pair(self.cards):
            return "2P"
        if is_one_pair(self.cards):
            return "1P"
        return "HC"

    def compare(self, other_hand):
        #if this hand wins, we return higher; if it loses, we return lower
        global hand_rank
        this_rank = hand_rank.index(self.rank)
        other_rank = hand_rank.index(other_hand.rank)
        if this_rank < other_rank:
            return "lower"
        elif other_rank < this_rank:
            return "higher"
        else:
            return tie_breaker(self, other_hand)

def generate_deck():
    global card_rank
    deck = []
    suits = ["C", "D", "H", "S"]
    for suit in suits:
        for rank in card_rank:
            deck.append(card(rank, suit))
    return deck
    
def unit_test():
    #global card_rank, hand_rank
    d = generate_deck()
    compare_card_vals1 = d[12].compare(d[11])
    assert compare_card_vals1 == "higher"
    compare_card_vals2 = d[10].compare(d[30])
    assert compare_card_vals2 == "higher"
    compare_card_vals3 = d[13].compare(d[40])
    assert compare_card_vals3 == "lower"
    compare_card_vals4 = d[39].compare(d[51])
    assert compare_card_vals3 == "lower"
    compare_card_vals5 = d[8].compare(d[47])
    assert compare_card_vals5 == "tie"
    compare_card_vals6 = d[15].compare(d[15])
    assert compare_card_vals6 == "tie"
    
    h1 = hand(d[21:26]) #TD JD QD KD AD
    assert h1.rank == "RF"

    h2 = hand(d[27:32]) #3H 4H 5H 6H 7H
    assert h2.rank == "SF"
    compare_hand_vals1 = h1.compare(h2)
    assert compare_hand_vals1 == "higher"
    h3 = hand(d[44:49]) #7S 8S 9S TS JS
    break_tie_sf = h3.compare(h2)
    assert break_tie_sf == "higher"
    
    h4 = hand([d[8], d[21], d[34], d[47], d[42]]) #TC TD TH TS 5S
    assert h4.rank == "4K"
    h5 = hand([d[9], d[22], d[35], d[48], d[43]]) #JC JD JH JS 6S
    break_tie_4k = h4.compare(h5)
    assert break_tie_4k == "lower"
    h6 = hand([d[9], d[22], d[35], d[48], d[44]]) #JC JD JH JS 7S
    break_tie_4k_kicker = h5.compare(h6)
    assert break_tie_4k == "lower"
    
    h7 = hand([d[2], d[15], d[46], d[33], d[20]]) #4C 4D 9S 9H 9D
    assert h7.rank == "FH"
    h8 = hand([d[2], d[15], d[45], d[32], d[19]]) #4C 4D 8S 8H 8D
    break_tie_fh_3k = h7.compare(h8)
    assert break_tie_fh_3k == "higher"
    h9 = hand([d[3], d[16], d[46], d[33], d[20]]) #5C 5D 9S 9H 9D
    break_tie_fh_1p = h9.compare(h7)
    assert break_tie_fh_1p == "higher"
    
    h10 = hand([d[13], d[15], d[16], d[17], d[21]]) #2D 4D 5D 6D TD
    assert h10.rank == "FL"
    h11 = hand([d[13], d[15], d[16], d[17], d[20]]) #2D 4D 5D 6D 9D
    break_tie_fl_highest = h11.compare(h10)
    assert break_tie_fl_highest == "lower"
    h12 = hand([d[13], d[15], d[16], d[18], d[20]]) #2D 4D 5D 7D 9D
    break_tie_fl_second = h11.compare(h12)
    assert break_tie_fl_second == "lower"
    h13 = hand([d[14], d[15], d[16], d[18], d[20]]) #3D 4D 5D 7D 9D
    break_tie_fl_lowest = h13.compare(h12)
    assert break_tie_fl_lowest == "higher"

    h14 = hand([d[4], d[18], d[19], d[7], d[34]]) #6C 7D 8D 9C TH
    assert h14.rank == "ST"
    h15 = hand([d[5], d[19], d[20], d[8], d[35]]) #7C 8D 9D TC JH
    break_tie_st = h15.compare(h14)
    assert break_tie_st == "higher"

    h16 = hand([d[16], d[29], d[42], d[13], d[9]]) #5D 5H 5S 2D JC
    assert h16.rank == "3K"
    h17 = hand([d[17], d[30], d[43], d[13], d[9]]) #6D 6H 6S 2D JC
    break_tie_3k_3k = h16.compare(h17)
    assert break_tie_3k_3k == "lower"
    h18 = hand([d[16], d[29], d[42], d[13], d[11]]) #5D 5H 5S 2D KC
    break_tie_3k_kicker = h16.compare(h18)
    assert break_tie_3k_kicker == "lower"
    h19 = hand([d[16], d[29], d[42], d[25], d[11]]) #5D 5H 5S AD KC
    break_tie_3k_2kicker = h19.compare(h18)
    assert break_tie_3k_2kicker == "higher"

    h20 = hand([d[10], d[36], d[24], d[39], d[11]]) #QC QH KD 2S KC
    assert h20.rank == "2P"
    h21 = hand([d[10], d[36], d[13], d[39], d[11]]) #QC QH 2D 2S KC
    break_tie_2p_top_pair = h21.compare(h20)
    assert break_tie_2p_top_pair == "lower"
    h22 = hand([d[9], d[35], d[24], d[39], d[11]]) #JC JH KD 2S KC
    break_tie_2p_second_pair = h20.compare(h22)
    assert break_tie_2p_second_pair == "higher"
    h23 = hand([d[10], d[36], d[24], d[40], d[11]]) #QC QH KD 3S KC
    break_tie_2p_kicker = h23.compare(h20)
    assert break_tie_2p_kicker == "higher"

    h24 = hand([d[15], d[7], d[47], d[35], d[28]]) #4D 9C TS JH 4H
    assert h24.rank == "1P"
    compare_hand_vals2 = h24.compare(h7)
    assert compare_hand_vals2 == "lower"
    h25 = hand([d[16], d[7], d[47], d[35], d[29]]) #5D 9C TS JH 5H
    break_tie_1p_pair = h25.compare(h24)
    assert break_tie_1p_pair == "higher"
    h26 = hand([d[15], d[7], d[47], d[36], d[28]]) #4D 9C TS QH 4H
    break_tie_1p_kicker = h26.compare(h24)
    assert break_tie_1p_kicker == "higher"
    h27 = hand([d[15], d[5], d[47], d[35], d[28]]) #4D 7C TS JH 4H
    break_tie_1p_3kicker = h27.compare(h24)
    assert break_tie_1p_3kicker == "lower"
    
    h28 = hand([d[34], d[9], d[14], d[42], d[25]]) #TH, JC, 3D, 5S, AD
    assert h28.rank == "HC"
    compare_hand_vals3 = h24.compare(h28)
    assert compare_hand_vals3 == "higher"
    h29 = hand([d[34], d[9], d[14], d[42], d[24]]) #TH, JC, 3D, 5S, KD
    break_tie_hc_kicker = h29.compare(h28)
    assert break_tie_hc_kicker == "lower"
    h30 = hand([d[33], d[9], d[14], d[42], d[25]]) #9H, JC, 3D, 5S, AD
    break_tie_hc_2kicker = h30.compare(h28)
    assert break_tie_hc_2kicker == "lower"
    h31 = hand([d[34], d[9], d[13], d[42], d[25]]) #TH, JC, 2D, 5S, AD
    break_tie_hc_5kicker = h31.compare(h28)
    assert break_tie_hc_5kicker == "lower"

def main():
    lines = [line.rstrip() for line in \
             open("Problem0054Data.txt", "r").readlines()]
    deck = generate_deck()
    d = {str(c) : c for c in deck}
    p1_wins = 0
    p2_wins = 0
    for line in lines:
        sline = line.split(" ")
        p1_cards = []
        p2_cards = []
        for i in range(5):
            p1_cards.append(d[sline[i]])
            p2_cards.append(d[sline[i+5]])
        p1_hand = hand(p1_cards)
        p2_hand = hand(p2_cards)
        result = p1_hand.compare(p2_hand)
        if result == "higher":
            p1_wins += 1
        elif result == "lower":
            p2_wins += 1
    return(p1_wins, p2_wins)
            

#unit_test()
print("Problem 54 solution: " + str(main()[0]))
