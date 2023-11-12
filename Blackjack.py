import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in range(1, 14)]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Player:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value > 10:
                self.value += 10
            elif card.value == 1:
                has_ace = True
                self.value += 11
            else:
                self.value += card.value

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display_cards(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())

class Game:
    def __init__(self):
        pass

    def play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player = Player()
            self.dealer = Player(dealer=True)

            for i in range(2):
                self.player.add_card(self.deck.deal())
                self.dealer.add_card(self.deck.deal())

            print("Welcome to Blackjack!")
            print("The game has started!")
            print("Your cards are:")
            self.player.display_cards()
            print("Dealer's cards are:")
            self.dealer.display_cards()

            game_over = False

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack)
                    continue

                choice = input("Please choose [Hit / Stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please enter 'hit' or 'stick' (or H/S) ").lower()
                if choice in ['hit', 'h']:
                    self.player.add_card(self.deck.deal())
                    self.player.display_cards()
                    if self.player.get_value() > 21:
                        print("You have busted! Dealer wins!")
                        game_over = True
                else:
                    player_value = self.player.get_value()
                    dealer_value = self.dealer.get_value()

                    print("Final Results")
                    print("Your cards:", self.player.cards)
                    print("Your value:", player_value)
                    print("Dealer's cards:", self.dealer.cards)
                    print("Dealer's value:", dealer_value)

                    if player_value > dealer_value:
                        print("You Win!")
                    elif player_value == dealer_value:
                        print("Tie!")
                    else:
                        print("Dealer Wins!")
                    game_over = True

            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thank you for playing!")
                playing = False
            else:
                game_over = False

    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player.get_value() == 21:
            player = True
        if self.dealer.get_value() == 21:
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw!")

        elif player_has_blackjack:
            print("You have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")

if __name__ == "__main__":
    g = Game()
    g.play()
