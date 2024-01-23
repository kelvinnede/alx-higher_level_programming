#!/usr/bin/python3
"""
This module contains a class Square that defines a square.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the value of the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the value of the size attribute.

        Args:
            value (float or int): The new size to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares if two Square instances are equal based on their area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares if two Square instances are not equal based on their area.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Compares if the area of the current Square instance is
        less than the area of another.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if less than, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares if the area of the current Square instance is
        less than or equal to the area of another.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if less than or equal to, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares if the area of the current Square instance is
        greater than the area of another.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if greater than, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares if the area of the current Square instance is
        greater than or equal to the area of another.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if greater than or equal to, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    Square = __import__('102-square').Square

    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
