# Cards Module
# Basic classes for a game with playing cards

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    VALUES = {"A":14, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
             "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
    
    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up
        
    def __eq__(self, other):
        if Card.VALUES[self.rank] == Card.VALUES[other.rank]:
            return True
        else:
            return False
    def __eq__(self, other):
        if Card.VALUES[self.rank] == other:
            return True
        else:
            return False
    def __add__(self, i):
        return Card.VALUES[self.rank]+i
    def __gt__(self, other):
        #print(other)
        if Card.VALUES[str(self.rank)] > Card.VALUES[str(other.rank)]:
            return True
        else:
            return False
    '''def __lt__(self, other):
        if Card.VALUES[self.rank] < other:
            return True
        else:
            return False'''   
      
class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
    def sort(self):
#        print("self.cards[i] ",self.cards[1])
        for i in range(0, len(self.cards)-1):
            for j in range(i+1, len(self.cards)):
                if self.cards[i]>self.cards[j]:
                    temp = self.cards[i]
                    self.cards[i] = self.cards[j]
                    self.cards[j] = temp

class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, dealer_hand, per_hand = 3):
        for rounds in range(per_hand):
            for hand in hands:
                if len(hand.cards) <3:
                    if self.cards:
                        top_card = self.cards[0]
                        self.give(top_card, hand)
                    else:
                        print("Can't continue deal. Out of cards!")
        self.dealer_deal(dealer_hand)
    def dealer_deal(self, hand):
        for i in range(0,2):
            if self.cards:
                top_card = self.cards[0]
                self.give(top_card, hand)
            else:
                print("Can't continue deal. Out of cards!")
        for card in hand.cards:
            card.flip()
    def stack(self):
        '''self.cards[0] = Card("K","h")
        self.cards[1] = Card("3","d")
        self.cards[2] = Card("K","d")
        self.cards[3] = Card("3","h")
        self.cards[4] = Card("Q","d")
        self.cards[5] = Card("3","c")
        '''
        self.cards[0] = Card("3","d")
        self.cards[1] = Card("5","c")
        self.cards[2] = Card("4","d")
        self.cards[3] = Card("10","c")
        self.cards[4] = Card("5","d")
        self.cards[5] = Card("Q","c")








#
#if __name__ == "__main__":
#    print("This is a module with classes for playing cards.")
#    input("\n\nPress the enter key to exit.")
