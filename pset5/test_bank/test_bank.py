from bank import value


def test_value_h():
    assert value("hi jack") == 20
    assert value("HI jack") == 20
    # assert value(" hi jack") == 20


def test_value_hello():
    assert value("hello jack") == 0
    # assert value(" hello jack") == 0
    # assert value(" Hello jack") == 0


def test_value_else():
    assert value("jack") == 100
    # assert value(" jack") == 100
    # assert value(" greetings jack") == 100
