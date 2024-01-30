#!/usr/bin/python3
"""Defines a square printing function."""


def print_square(size):
    """Print a square with the # char.

    Args:
        size (int): The height or width of the square.
    Raises:
        TypeError: If size is not an int.
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
