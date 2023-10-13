import pytest
from plates import is_valid


def test_min_max():
    assert not is_valid('c')
    assert not is_valid('maximus01')


def test_two_first_letters():
    assert is_valid('xdMa1')
    assert not is_valid('d66g')


def test_number_interrupted_by_the_letter():
    assert not is_valid('CS50P')


def test_no_punctuation():
    assert not is_valid('PI3.14')


def test_cs50():
    assert is_valid('CS50')
    assert not is_valid('CS05')
    assert not is_valid('CS50P')
    assert not is_valid('PI3.14')
    assert not is_valid('H')
    assert not is_valid('OUTATIME')


def test_plate_begins_with_alphabetical_character():
    assert not is_valid("123456")
    assert is_valid("ABC123")