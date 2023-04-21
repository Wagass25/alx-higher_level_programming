#!/usr/bin/python3
"""
Unittests for Base Class
"""
import unittest
import json
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test Base Class"""

    @classmethod
    def setClass(cls):
        """
        Test object instantiate
        """

        cls.one = Base()
