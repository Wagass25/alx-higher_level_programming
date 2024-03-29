#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"

    Args:
        first_name (str): The first name.
        last_name (str): The last name, if provided.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
