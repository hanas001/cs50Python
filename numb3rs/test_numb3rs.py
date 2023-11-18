import pytest
from numb3rs import validate

def test_validate_word():
    assert not validate('cat')

def test_validate_correct():
    assert validate('127.0.0.1')
    assert validate('255.255.255.255')

def test_validate_incorrect():
    assert not validate('512.512.512.512')
    assert not validate('1.2.3.1000')

def test_validate_first_byte_range():
    assert validate('1.2.3.4')
    assert validate('127.0.0.1')
    assert validate('223.255.255.255')
    assert validate('0.0.0.0')
    assert validate('224.0.0.1')
    assert validate('255.255.255.255')