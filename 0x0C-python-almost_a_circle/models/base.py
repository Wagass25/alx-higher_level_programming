#!/usr/bin/python3
"""
Base class for all models
"""

import json
import csv
import os
import turtle


class Base:
    """
    Base class for all models
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            with open(filename, "w") as f:
                f.write(cls.to_json_string(list(map(lambda x:
                                                    x.to_dictionary(),
                                                    list_objs))))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return [cls.create(**d) for d in
                        cls.from_json_string(f.read())]
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in CSV
        """
        fname = cls.__name__ + ".csv"

        if list_objs is None:
            with open(fname, "w") as cfile:
                cfile.write("[]")
        else:
            with open(fname, "w") as cfile:
                writer = csv.writer(cfile)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.width, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes from CSV and returns a list of instances
        """
        fname = cls.__name__ + ".csv"

        with open(fname, "r") as cfile:
            if cls.__name__ == "Rectangle":
                reader = csv.DictReader(
                    cfile, fieldnames={'id', 'width', 'height', 'x', 'y'})
            elif cls.__name__ == "Square":
                reader = csv.DictReader(
                    cfile, fieldnames={'id', 'size', 'x', 'y'})

            instances = []
            for instance in reader:
                instance = {x: int(y) for x, y in instance.items()}
                temp = cls.create(**instance)
                instances.append(temp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw the rectangles and squares
        """
        t = turtle.Turtle()
