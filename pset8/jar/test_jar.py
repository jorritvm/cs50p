import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12  # calls the getter method


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(5)
