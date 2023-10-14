import pytest

from fuel import convert, gauge

@pytest.mark.parametrize("fraction,expected_percentage", [
    ("1/2", 50),
    ("1/3", 33),
    ("1/4", 25),
    ("1/5", 20),
])
def test_convert_valid_fraction(fraction, expected_percentage):
    percentage = convert(fraction)
    assert percentage == expected_percentage

@pytest.mark.parametrize("fraction", ["1/0", "-1/2", "2.5/3"])
def test_convert_invalid_fraction(fraction):
    with pytest.raises(ValueError):
        convert(fraction)

@pytest.mark.parametrize("percentage,expected_gauge_result", [
    (0, "E"),
    (100, "F"),
])
def test_gauge_valid_percentage(percentage, expected_gauge_result):
    gauge_result = gauge(percentage)
    assert gauge_result == expected_gauge_result

@pytest.mark.parametrize("percentage", [-1, 101])
def test_gauge_invalid_percentage(percentage):
    with pytest.raises(ValueError):
        gauge(percentage)