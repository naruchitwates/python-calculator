import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(3, 1)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)
