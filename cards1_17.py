import random
#pylint: disable=no-member
#pylint: disable=unused-variable
class Card():
    def __init__(self,r,s):
        self.rank = r
        self.suit = s

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @rank.setter
    def rank(self,r):
        self._rank = r

    @suit.setter
    def suit(self,s):
        self._suit = s

    def show_card(self):
        print(f"{self.rank} of {self.suit}")

class Deck():
    # Initialize a 52-card deck
    def __init__(self):
        self.cards = []
        rank = [x for x in range(1,11)] + ["Jack","Queen","King"]
        suit = ["Hearts","Spades","Clubs","Diamonds"]
        for r in rank:
            for s in suit:
                self.cards.append(Card(r,s))

    def show_deck(self):
        for c in self.cards:
            print(f"Rank: {c.rank}, Suit: {c.suit}")
    
    def shuffle(self):
        random.shuffle(self.cards)

            

# Player class
class Player():
    def __init__(self,n):
        self.name = n
        self.hand = []
        self.money = 1000.0
    
    def draw(self,deck,n):
        for i in range(n):
            if not deck.cards:
                print("Deck is empty!")
                break
            else:
                self.hand.append(deck.cards.pop())

    def show_hand(self):
        if not self.hand:
            print("Hand is empty!")
        else:
            print(f"{self.name}'s Hand:")
            for c in self.hand:
                c.show_card()
            print("\n")
        return
    



def main():
    d = Deck()
    d.shuffle()

    player1 = Player("Player1")
    player2 = Player("Player2")
    
    player1.draw(d,50)
    player2.draw(d,2)
    
    player1.show_hand()
    player2.show_hand()


    
main() 
