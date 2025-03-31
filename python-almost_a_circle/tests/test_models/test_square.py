import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def test_square_instance(self):
        """Test Square instance creation."""
        s = Square(10, 2, 3, 99)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 99)

    def test_square_size_setter(self):
        """Test size setter updates width and height."""
        s = Square(10)
        s.size = 20
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)

    def test_square_size_validation(self):
        """Test validation for incorrect size values."""
        with self.assertRaises(TypeError):
            Square("10")
        with self.assertRaises(ValueError):
            Square(-10)

    def test_update_args(self):
        """Test update with *args."""
        s = Square(5, 1, 1, 101)
        s.update(200, 15, 3, 4)
        self.assertEqual(s.id, 200)
        self.assertEqual(s.size, 15)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with **kwargs."""
        s = Square(5, 1, 1, 101)
        s.update(id=300, size=25, x=6, y=7)
        self.assertEqual(s.id, 300)
        self.assertEqual(s.size, 25)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

    def test_to_dictionary(self):
        """Test dictionary representation of Square."""
        s = Square(10, 2, 3, 99)
        expected_dict = {"id": 99, "size": 10, "x": 2, "y": 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()