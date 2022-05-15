import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_myltiply_calcilate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_calcilate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calcilate_correctly(self):
        assert self.calc.subtraction(self, 25, 12) == 13

    def test_adding_calcilate_correctly(self):
        assert self.calc.adding(self, 11, 21) == 32