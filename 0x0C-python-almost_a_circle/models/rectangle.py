#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle implements Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class

            Args:
                width: width of the rectangle
                height: height of the rectangle
                x: x coordinate of the rectangle
                y: y coordinate of the rectangle
                id: id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter for x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter for y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            prints rectangle to stdout with instance "#"
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
            returns string representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
            assigns an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
            returns the dictionary representation of the rectangle
        """
        return {"x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width
                }
