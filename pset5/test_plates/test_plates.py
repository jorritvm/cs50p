from plates import is_valid


def test_plates_start_with_two_letters():
    assert is_valid("HELLO") == True
    assert is_valid("1ELLO") == False
    assert is_valid("H2LLO") == False
    assert is_valid("12LLO") == False
    assert is_valid("HH") == True
    assert is_valid("11") == False


def test_plates_between_2_and_6_char():
    assert is_valid("HELLO") == True
    assert is_valid("H") == False
    assert is_valid("ABCDEFG") == False


def test_plates_numbers_at_end():
    assert is_valid("HELL1") == True
    assert is_valid("HE11O") == False


def test_plates_first_number_nonzero():
    assert is_valid("HELL10") == True
    assert is_valid("HELL01") == False


def test_plates_no_special_char():
    assert is_valid("HELLO!") == False
    assert is_valid("HELL0 ") == False
