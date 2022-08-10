import cowsay
from players import Human, Dealer
from time import sleep


def print_values(human, dealer):
    dc = dealer.count()
    if dc > 21:
        dc = "BUST"

    hc = human.count()
    if hc > 21:
        hc = "BUST"

    print("\n")
    print(f"----- Dealer {dc}----")
    print(dealer.hand)
    print(f"----- Human {hc}-----")
    print(human.hand)


def print_money(human):
    print("Money: " + str(human.money))


def print_game_over():
    cowsay.dragon("GAME OVER")


def decide_winner(hc, dc):
    # If both the player and the dealer go bust, the player loses his bet.
    if hc > 21 and dc > 21:
        winner = "dealer"
    # If only the player goes bust, the player loses his bet.
    elif hc > 21 and dc <= 21:
        winner = "dealer"
    # If only the dealer goes bust, the player wins and receives the same amount as his bet.
    elif hc <= 21 and dc > 21:
        winner = "human"
    # If the player has a closer count to 21 than the dealer, the player wins and receives the same amount as his bet.
    elif hc > dc:
        winner = "human"
    # If the dealer has a closer count to 21 than the player, the player loses his bet.
    elif hc < dc:
        winner = "dealer"
    # If both the dealer and player have the same count, it is a **stand-off** and the player's bet returns to his purse.
    elif hc == dc:
        winner = "draw"
    return winner


def decide_impact_on_money(winner, bet):
    if winner == "dealer":
        impact = -1 * bet
    elif winner == "human":
        impact = bet
    elif winner == "draw":
        impact = 0
    return impact


def main():
    # create the players
    human = Human(1000)
    dealer = Dealer()

    while human.money > 0:
        # bet
        print_money(human)
        bet = human.bet()

        # deal
        human.hand = dealer.deck.deal(2)
        dealer.hand = dealer.deck.deal(1)
        dealer.hidden_hand = dealer.deck.deal(1)

        print_values(human, dealer)

        # human play
        human.is_playing = True
        while human.is_playing:
            if human.hit_or_stand() == "+":
                human.hand += dealer.deck.deal(1)
                if human.count() > 21:
                    human.is_playing = False
            else:
                human.is_playing = False

            print_values(human, dealer)

        # unveil dealer card
        sleep(1)  # add suspense!
        dealer.unveil_hidden_card()
        print_values(human, dealer)

        # dealer play
        dealer.is_playing = True
        while dealer.is_playing:
            sleep(1)  # add suspense!
            if dealer.hit_or_stand() == "+":
                dealer.hand += dealer.deck.deal(1)
                if dealer.count() > 21:
                    dealer.is_playing = False
            else:
                dealer.is_playing = False

            print_values(human, dealer)

        # decide winner
        winner = decide_winner(human.count(), dealer.count())
        print("\nWinner is: " + winner)

        # adjust the money balance
        impact = decide_impact_on_money(winner, bet)
        human.money += impact

        # the easiest reset for next round is to create 2 new instances,
        # with adjusted money for the human
        human = Human(human.money)
        dealer = Dealer()

    print_game_over()


if __name__ == "__main__":
    main()
