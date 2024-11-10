import unittest
from src.utils.validators import validate_probabilities, validate_lengths_and_probabilities

class TestValidators(unittest.TestCase):
    
    def test_validate_probabilities(self):
        self.assertTrue(validate_probabilities([0.5, 0.5]))
        self.assertTrue(validate_probabilities([0.2, 0.3, 0.5]))
        self.assertFalse(validate_probabilities([0.1, 0.9, 0.1]))
        self.assertFalse(validate_probabilities([-0.1, 1.1]))
    
    def test_validate_lengths_and_probabilities(self):
        self.assertTrue(validate_lengths_and_probabilities([1, 2, 3], [0.2, 0.3, 0.5]))
        self.assertFalse(validate_lengths_and_probabilities([1, 2], [0.2, 0.3, 0.5]))
        self.assertFalse(validate_lengths_and_probabilities([1, 2, 3], [0.1, 0.2, 0.8]))

if __name__ == '__main__':
    unittest.main()
