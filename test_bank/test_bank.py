import pytest

from bank import value


def test_value_hello():
    assert value('hello') == 0


def test_value_h():
    assert value('h') == 20


def test_value_other():
    assert value('bla') == 100


def test_case_insensitivity():
    assert value('Hi') == 20
    assert value('hELLO') == 0
    assert value('What\'s up') == 100