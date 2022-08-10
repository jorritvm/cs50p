from project import decide_winner, decide_impact_on_money, print_money
from players import Human


def test_decide_winner():
    assert decide_winner(18, 18) == "draw"
    assert decide_winner(18, 19) == "dealer"
    assert decide_winner(21, 18) == "human"


def test_decide_impact_on_money():
    assert decide_impact_on_money("draw", 500) == 0
    assert decide_impact_on_money("dealer", 500) == -500
    assert decide_impact_on_money("human", 500) == 500


def test_print_money(capfd):
    print_money(Human(1000))
    out, err = capfd.readouterr()
    assert out == "Money: 1000\n"
