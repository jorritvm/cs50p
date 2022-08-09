from um import count
import pytest


def test_count_um():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("yummy") == 0


def test_case():
    assert count("Um") == 1
    assert count("Um Um") == 2
    assert count("yUmmy") == 0


def test_punctuation():
    assert count("um?") == 1
    assert count("um!") == 1
