import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit test class for max_integer function"""

    def test_positive_numbers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative integers"""
        self.assertEqual(max_integer([-10, 50, 0, 30, -5]), 50)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test with a list that has only one element"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicates(self):
        """Test with duplicate values"""
        self.assertEqual(max_integer([4, 4, 4, 4, 4]), 4)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([10, 5, 20, 15]), 20)

    def test_max_at_start(self):
        """Test where the max number is at the beginning"""
        self.assertEqual(max_integer([100, 10, 20, 30]), 100)

    def test_max_at_end(self):
        """Test where the max number is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 99]), 99)

if __name__ == '__main__':
    unittest.main()