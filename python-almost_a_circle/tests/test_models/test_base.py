import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Reset Base class object counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test that id auto-increments correctly."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_custom(self):
        """Test that custom id is assigned properly."""
        b1 = Base(100)
        b2 = Base(200)
        self.assertEqual(b1.id, 100)
        self.assertEqual(b2.id, 200)

    def test_mixed_ids(self):
        """Test a mix of custom and auto-incremented ids."""
        b1 = Base()
        b2 = Base(50)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 50)
        self.assertEqual(b3.id, 2)  # Auto-increment continues

    def test_to_json_string(self):
        """Test JSON serialization of a dictionary list."""
        dict_list = [{"id": 1, "name": "test"}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 1, "name": "test"}]')

    def test_to_json_string_empty(self):
        """Test JSON serialization of an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Test JSON deserialization into a dictionary list."""
        json_str = '[{"id": 1, "name": "test"}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 1, "name": "test"}])

    def test_from_json_string_empty(self):
        """Test JSON deserialization from an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

if __name__ == "__main__":
    unittest.main()