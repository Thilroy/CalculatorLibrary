"""
Unit tests for the calculator library
"""
from calculator import utils


class TestCalculator:

    def test_addition(self):
        assert 4 == utils.add(2, 2)

    def test_subtraction(self):
        assert 2 == utils.subtract(4, 2)