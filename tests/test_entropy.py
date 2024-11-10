import unittest
from src.calculations.entropy import calcola_entropia

class TestEntropyCalculation(unittest.TestCase):
    
    def test_single_probability(self):
        self.assertAlmostEqual(calcola_entropia([0.5]), 1.0, places=6)
    
    def test_multiple_probabilities(self):
        self.assertAlmostEqual(calcola_entropia([0.4, 0.6]), 0.970951, places=6)
    
    def test_zero_probability(self):
        self.assertAlmostEqual(calcola_entropia([1.0]), 0.0, places=6)

if __name__ == '__main__':
    unittest.main()
