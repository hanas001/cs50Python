from twttr import shorten
import pytest

def test_problem_set_test():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('What\'s your name?') == 'Wht\'s yr nm?'
    assert shorten('CS50') == 'CS50'


def test_capital_letters():
    assert shorten('tWItter') == 'tWttr'
    assert shorten('WhAt\'s yOUr namE?') == 'Wht\'s yr nm?'