#!/usr/bin/python3

"""
This module contains a function that adds two integers
"""

def add_integer(a, b=98):
    """
    Adds two integers a and b

    Args:
        a (int/float): The first number.
        b (int/float): The second number. Defaaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
