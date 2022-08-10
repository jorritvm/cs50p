import pydealer


class Player:
    def __init__(self):
        self.hand = None
        self.is_playing = False
        self.handtype = "Hard Hand"

    def count(self):
        self.hardhand = "Hard Hand"
        count = 0
        for card in self.hand:
            cv = card.value
            if cv.isnumeric():
                count += int(cv)
            elif cv.lower() in ["jack", "queen", "king"]:
                count += 10
            elif cv.lower() == "ace":
                if count + 11 <= 21:
                    count += 11
                else:
                    count += 1
                    self.hardhand = "Soft Hand"
        return count


class Human(Player):
    def __init__(self, money):
        self.money = money

    def bet(self):
        while True:
            try:
                user_bet = int(input("Bet: "))
                if user_bet <= 0 or user_bet > self.money:
                    raise ValueError
                return user_bet
            except:
                pass

    def hit_or_stand(self):
        while True:
            try:
                user_hit_stand = input("Hit (+) or stand (-)? ")
                print("user said: '" + user_hit_stand + "'")
                if not user_hit_stand in ["+", "-"]:
                    raise ValueError
                return user_hit_stand
            except:
                pass


class Dealer(Player):
    def __init__(self):
        self.hidden_hand = None
        self.new_game()

    def new_game(self):
        self.deck = pydealer.Deck()
        self.deck.shuffle()

    def unveil_hidden_card(self):
        self.hand += self.hidden_hand
        self.hidden_hand = None

    def hit_or_stand(self):
        if self.count() >= 17:
            return "-"
        else:
            return "+"
