from seasons import date_checker
from seasons import Date
import pytest

def test_date():
    with pytest.raises(SystemExit):
        date_checker('cat')
        date_checker('20244-04-01')
        date_checker('2020-433-02')
        date_checker('2019-03-111')

def test_date_splitter():
    date_str = '2021-11-01'
    date = Date(date_str)
    year, month, day = date.date_splitter()
    assert year == 2021
    assert month == 11
    assert day == 1

    with pytest.raises(SystemExit):
        date_str = '2021-11-31'
        date = Date(date_str)
        date.date_splitter()