import json
import os
import csv
import turtle
import random

class Base:
    """Base class to manage id attribute across all other classes."""

    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """Class constructor for Base.

        Args:
            id (int, optional): The ID of the instance. If None, auto-increments.
        """
        if id is not None:
            self.id = id  # Assign id if provided
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # Auto-assign a unique

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string into a list of dictionaries.

        Args:
            json_string (str): JSON string representation of a list of dictionaries.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set from a dictionary.

        Args:
            dictionary (dict): Dictionary of attributes to set.

        Returns:
            An instance of cls with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Creating a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Creating a dummy Square instance
        else:
            return None  # If it's neither, return None

        dummy.update(**dictionary)  # Use the update method to set attributes
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file.

        - The filename is `<Class name>.json`.
        - If the file doesn’t exist, return an empty list.
        """
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):  # Check if the file exists
            return []

        with open(filename, "r", encoding="utf-8") as f:
            json_data = f.read()

        dict_list = cls.from_json_string(json_data)  # Convert JSON to a list of dictionaries
        return [cls.create(**d) for d in dict_list]  # Convert to instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and saves instances into a CSV file."""
        filename = f"{cls.__name__}.csv"
        fieldnames = []

        # Define fieldnames based on class type
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]

        # Write to CSV
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())  # Convert each object to a dictionary

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file and returns a list of objects."""
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):  # If file doesn't exist, return an empty list
            return []

        with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            list_dicts = [dict(row) for row in reader]  # Convert rows to a list of dictionaries

        # Convert dictionary values from strings to integers
        for d in list_dicts:
            for key in d:
                d[key] = int(d[key])

        return [cls.create(**d) for d in list_dicts]  # Convert dictionaries to instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a Turtle graphics window and draws all rectangles and squares."""
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Rectangles and Squares Drawing")

        pen = turtle.Turtle()
        pen.speed(3)

        # Function to draw a shape
        def draw_shape(shape):
            """Draws a rectangle or square using Turtle graphics."""
            pen.penup()
            pen.goto(shape.x, -shape.y)  # Move to the starting position
            pen.pendown()
            pen.color(random.choice(["red", "blue", "green", "orange", "purple"]))

            pen.begin_fill()
            for _ in range(2):  # Draw rectangle or square
                pen.forward(shape.width)
                pen.left(90)
                pen.forward(shape.height)
                pen.left(90)
            pen.end_fill()

        # Draw all rectangles
        for rect in list_rectangles:
            draw_shape(rect)

        # Draw all squares
        for sq in list_squares:
            draw_shape(sq)

        # Keep the window open
        turtle.done()
