import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0") is True
    with pytest.raises(ValueError):
        assert convert("10/1") is True


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
