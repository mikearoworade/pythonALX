import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_rectangle_instance(self):
        """Test Rectangle instance creation."""
        r = Rectangle(10, 20, 5, 5, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 1)

    def test_rectangle_validation(self):
        """Test validation for incorrect values."""
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)
        with self.assertRaises(ValueError):
            Rectangle(10, -20)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 5)

    def test_area(self):
        """Test calculation of rectangle area."""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_update_args(self):
        """Test the update method with *args."""
        r = Rectangle(10, 10, 1, 1, 100)
        r.update(200, 20, 30, 2, 3)
        self.assertEqual(r.id, 200)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        r = Rectangle(10, 10, 1, 1, 100)
        r.update(id=200, width=30, height=40, x=5, y=6)
        self.assertEqual(r.id, 200)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        """Test dictionary representation of Rectangle."""
        r = Rectangle(10, 20, 5, 5, 1)
        expected_dict = {"id": 1, "width": 10, "height": 20, "x": 5, "y": 5}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()