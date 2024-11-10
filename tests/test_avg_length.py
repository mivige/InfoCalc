import unittest
from src.calculations.avg_length import calcola_lunghezza_media

class TestAvgLengthCalculation(unittest.TestCase):
    
    def test_avg_length(self):
        self.assertAlmostEqual(calcola_lunghezza_media([1, 2, 3], [0.2, 0.3, 0.5]), 2.3, places=6)

    def test_zero_probabilities(self):
        self.assertAlmostEqual(calcola_lunghezza_media([1, 2, 3], [0, 0, 1]), 3.0, places=6)

if __name__ == '__main__':
    unittest.main()
