from watch import parse
import pytest
import re

def test_parse():
    assert parse("<iframe src='http://www.youtube.com/embed/xvFZjo5PgG0'></iframe>") == "https://youtu.be/xvFZjo5PgG0"