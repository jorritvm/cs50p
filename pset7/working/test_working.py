from working import convert
import pytest


def test_convert_am_to_am():
    assert convert("9:00 AM to 11:00 AM") == "09:00 to 11:00"


def test_convert_pm_to_pm():
    assert convert("8:00 PM to 10:00 PM") == "20:00 to 22:00"


def test_convert_am_to_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert_pm_to_am():
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"


def test_convert_invalid():
    with pytest.raises(ValueError):
        assert convert("lmkjqsdflmkj") is True
