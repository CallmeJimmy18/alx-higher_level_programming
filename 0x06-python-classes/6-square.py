#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialises a new Square

        Args:
            size (int): this is the size of the square
            position (int)(int): position of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """Gets current pos of new square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """This is the squared area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a Square in Stdout"""
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__size):
            [print(" ") for k in range(0, self.__position[0])]
            for j in range(self.__size):
                print("#", end="")
            print("")
