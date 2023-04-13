#!/usr/bin/python3
"""``Student`` class module"""


class Student:
    """A class the represent a student"""

    def __init__(self, first_name, last_name, age):
        """Sets attributes of a new Student instance

            Args:
                first_name (str): The first name
                last_name (str): The last name
                age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a json represent of Student"""
        r = {}
        for key in self.__dict__:
            value = getattr(self, key)
            if type(value) in [list, dict, str, int, bool]:
                r[key] = value
        return r
