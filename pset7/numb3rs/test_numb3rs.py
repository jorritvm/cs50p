from numb3rs import validate


def test_validate_args_amount():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.4.5") == False


def test_validate_args_range():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.400") == False
