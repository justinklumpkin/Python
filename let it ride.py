import cards, games, random#, playing_cards, playing_cards2, playing_cards3

'''d = cards.Deck()
print("empty deck: ",d)
d.populate()
d.shuffle()
print("shuffled deck ",d)
p = games.Player("Potter")
dealer_hand = cards.Hand()

h = []
for i in range(0, 3):
    h.append(cards.Hand())

d.deal(h, dealer_hand)

print("\n\nHands: ")
for hand in h:
    print(hand, "\n")
print("Dealer hand: ",dealer_hand)'''
##c1 = cards.Card("4", "c")
##c2 = cards.Card("4", "h")
##c3 = cards.Card("Q", "s")
##c4 = cards.Card("J", "d")
##c5 = cards.Card("K", "c")
###h.append(cards.Hand())
##h= cards.Hand()
###d.deal(h, 3)
##h.add(c1)
##h.add(c2)
##h.add(c3)
##

##dealer_hand.add(c4)
##dealer_hand.add(c5)
##
##'''d.dealer_deal(dealer_hand)
##print("\n",h[0], "\n", dealer_hand)'''
##
##p = games.Player("Justin")
##print(p)
##p.new_hand(h)
##
##print(p.check_winning_hand(dealer_hand))



class letItRide():
    PAYOUTS = {"royal flush":1000, "straight flush":200, "4 of a kind":50, "full house":11, 
               "flush":8, "straight":5, "3 of a kind":3, "2 pair":2, "pair of 10+":1, "you lost":0}
    BONUS_PAY = {'mimi royal':50, 'straight flush':40, '3 of a kind':30, 'flush':4,'straight':6, 'pair':1, 'you lost':0}
    def __init__(self):
        self.deck = cards.Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.deck.stack()#for grading
        self.players = []
        self.dealer_hand = cards.Hand()
        self.start()
    def start(self):
        numplayers = int(input("How many players are there?\n"))
        for i in range(0,numplayers):
            n = input("What's player " +str(i+1)+"'s name?\n")
            self.players.append(games.Player(n))
        self.game()
        self.payout()
    def game(self):
        GUARANTEED={'10':'10','11':'J','12':'Q','13':'K','14':'A'}
        for player in self.players:
            #base bet
            bet=games.ask_number( ("How much would " +player.name +" like to bet for each of 3 bets? (min $5)\n$"), 5, int(player.balance/3))
            player.alt_balance(-3*bet)
            player.set_bet(bet)
            

            #bonus bet
            bonus_bet = games.ask_yes_no(("Would " +player.name +" like to bonus bet $2? (y/n)\n"))
            if bonus_bet =='y':
                player.alt_balance(-2)
                player.set_bonus_bet(2)

            #tip dealer            
            tip = games.ask_yes_no("Would " +player.name +" like to tip $10 to the dealer? (y/n)\n")
            if tip=='y':
                rand = random.randint(10,14)
                player.alt_balance(-10)
                i=self.deck.cards.index(cards.Card(GUARANTEED[str(rand)],"s"))#suit doesn't matter in the __eq__ method 
                self.deck.give(self.deck.cards[i], player)
                #^that is better than this-->player.add(self.deck.cards[i])
                
        
        self.deck.deal(self.players,self.dealer_hand)
        print("\n\nHands: ")
        for p in self.players:            
            print(str(p), "\n")
        print("Dealer hand: ",self.dealer_hand)
        
        
        for player in self.players:
            pull_back=games.ask_yes_no("Would " + player.name+" like to pull back a bet? (y/n)\n")
            if pull_back == 'y':
                player.pull_back()

        print("\n\nHands: ")
        for p in self.players:            
            print(str(p), "\n")
        self.dealer_hand.cards[0].flip()
        print("Dealer hand: ",self.dealer_hand)
        
        for player in self.players:
            pull_back=games.ask_yes_no("Would " + player.name+" like to pull back a bet? (y/n)\n")
            if pull_back == 'y':
                player.pull_back()

        print("\n\nHands: ")
        for p in self.players:            
            print(str(p), "\n")
        self.dealer_hand.cards[1].flip()
        print("Dealer hand: ", self.dealer_hand)
        print("--------------------------------")
    def payout(self):
        for player in self.players:
            bbwin = player.check_bb()
            bbpay = letItRide.BONUS_PAY[bbwin]
            print(bbwin)
            if player.bonus!=0 and bbpay>0:
                player.alt_balance(bbpay*player.bonus+player.bonus)
            player.set_bonus_bet(0)
            
            win = player.check_winning_hand(self.dealer_hand)
            payout_rate = letItRide.PAYOUTS[win]
            while player.bets:
                bet = player.bets.pop()
                if payout_rate>0:
                    player.alt_balance(payout_rate*bet+bet)
            print(str(player), "\n\t"+ win.title()+" on the regular bet","\n\t"+bbwin.title()+" on the bonus")   
                
        
        
l = letItRide()
