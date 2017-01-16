"""Create random passwords easily."""

from string import digits, ascii_letters
from random import choice


def random_password(length=8, characters=digits + ascii_letters):
    """Create a password of exactly length characters long, made up of the
    characters found in characters. characters can be any iterable."""
    return ''.join(choice(characters) for x in range(length))
