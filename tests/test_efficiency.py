import unittest
from src.calculations.efficiency import calcola_efficienza

class TestEfficiencyCalculation(unittest.TestCase):
    
    def test_efficiency(self):
        self.assertAlmostEqual(calcola_efficienza(1.0, 1.2), 0.833333, places=6)
    
    def test_zero_length(self):
        with self.assertRaises(ZeroDivisionError):
            calcola_efficienza(1.0, 0)

if __name__ == '__main__':
    unittest.main()
