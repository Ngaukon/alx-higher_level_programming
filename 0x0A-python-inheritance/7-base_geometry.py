#!/usr/bin/python3
"""Defines the  class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """Class BaseGeometry.
    """
    def area(self):
        """Area functions.

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str): name of the objects.
            value (int): value of the property.

        Raises:
            TypeError: if value is not an integers.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
