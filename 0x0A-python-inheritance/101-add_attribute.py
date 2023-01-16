#!/usr/bin/python3
"""101-add_attribute Module"""


def add_attribute(obj, name, value):
    """add new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
