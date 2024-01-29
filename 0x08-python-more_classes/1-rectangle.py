#!/usr/bin/python3
"""

Module for defining a Rectangle class.
"""


class Rectangle:
    """
    Defines a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """
            Getter method for the width attribute.

            Returns:
                int: The width of the rectangle.
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            Setter method for the width attribute.

            Args:
                value (int): The value to set as the width.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """
            Getter method for the height attribute.

            Returns:
                int: The height of the rectangle.
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter method for the height attribute.

            Args:
                value (int): The value to set as the height.

            Raises:
                TypeError: If the value is not an integer.
                ValueError: If the value is less than 0.
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)