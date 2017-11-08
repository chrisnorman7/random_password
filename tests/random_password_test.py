from random_password import random_password


def test_defaults():
    assert len(random_password()) is 8


def test_with_length():
    length = 96
    assert len(random_password(length=length)) == length


def test_characters():
    chars = 'h'
    assert random_password(characters=chars) == chars * 8
