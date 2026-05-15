# test_app.py
import unittest
from app import calculate_revenue, ingredient_cost

class TestInventory(unittest.TestCase):
    def test_revenue(self):
        # 100 portions * 15 PLN = 1500 expected
        self.assertEqual(calculate_revenue(100, 15), 1500)

    def test_cost(self):
        # (5 * 3.0) + (10 * 8.0) = 15.0 + 80.0 = 95.0 expected
        self.assertEqual(ingredient_cost(5, 10), 95.0)

if __name__ == '__main__':
    unittest.main()