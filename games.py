# Games
# Demonstrates module creation
import cards
class Player(cards.Hand):
    """ A player for a game. """
    def __init__(self, name, balance = 100, c = [], bb=0):
        super(Player, self).__init__()
        self.name = name
        self.balance = balance
        self.bets = []
        self.bonus=bb
    def __str__(self):
        rep = self.name + ": $" + str(self.balance)+"\n\tHand: "+super(Player, self).__str__()+"\n\tTotal Bet: "+str(sum(self.bets))+"\n\tBonus Bet: "+str(self.bonus)
        return rep
    
    def new_hand(self, c):
        self.cards = c
    def check_bb(self):
        straight_count = 1
        flush_count = {"s":0, "h":0, "c":0,"d":0}
        pair_count = {"A":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,
             "8":0, "9":0, "10":0, "J":0, "Q":0, "K":0}

        #straight flush
        for card in self.cards:
            flush_count[card.suit]+=1
        '''print(self.hand.cards[0])'''
        for i in range(1, len(self.cards)):
            if self.cards[i] == self.cards[0]+i:
                straight_count+=1
        if straight_count == 3 and (3 in flush_count.values()):
            if self.cards[0].rank == 'Q':
                return "royal flush"
            else:
                return "straight flush"
        #flush
        if 3 in flush_count.values():
            return "flush"
        #straight
        if straight_count ==3:
            return "straight"
        #3 of a kind
        for card in self.cards:
            pair_count[card.rank]+=1
        if 3 in pair_count.values():
            return "3 of a kind"
        #pair
        if 2 in pair_count.values():
            return "pair"
        return "you lost"
    def check_winning_hand(self, dealer):
        straight_count = 1
        flush_count = {"s":0, "h":0, "c":0,"d":0}
        pair_count = {"A":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,
             "8":0, "9":0, "10":0, "J":0, "Q":0, "K":0}
        for card in dealer.cards:
            self.add(card)#working
        self.cards.sort()
        '''print(self.cards)'''

        #straight flush
        for card in self.cards:
            flush_count[card.suit]+=1
        '''print(self.hand.cards[0])'''
        for i in range(1, len(self.cards)):
            if self.cards[i] == self.cards[0]+i:
                straight_count+=1
        if straight_count == 5 and (5 in flush_count.values()):
            if self.cards[0].rank == '10':
                return "royal flush"
            else:
                return "straight flush"
        #4 of a kind
        for card in self.cards:
            pair_count[card.rank]+=1
        if 4 in pair_count.values():
            return "4 of a kind"
        #full house
        '''print(pair_count)'''
        if 3 in pair_count.values() and 2 in pair_count.values():
            return "full house"
        #flush
        if 5 in flush_count.values():
            return "flush"
        #straight
        if straight_count ==5:
            return "straight"
        #3 of a kind
        if 3 in pair_count.values():
            return "3 of a kind"
        #2 pair
        pairs = 0
        for item in pair_count.values():
            if item ==2:
                pairs+=1
        if pairs==2:
            return "2 pair"
        #pair of 10s or higher
        if pair_count["10"] == 2 or pair_count["J"]== 2 or pair_count["Q"]== 2 or pair_count["K"] == 2 or pair_count["A"]== 2:
            return "pair of 10+"
        return "you lost"
    def alt_balance(self, amount):#adds amount to balance (can be negative)
        self.balance = self.balance+amount
    def set_bet(self, b):
        for i in range(0,3):
            self.bets.append(b)
    def pull_back(self):
        self.balance+= self.bets.pop()
    def set_bonus_bet(self, amount):
        self.bonus = amount

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

  
#if __name__ == "__main__":
#    print("You ran this module directly (and did not 'import' it).")
#    input("\n\nPress the enter key to exit.")


