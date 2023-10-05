#!/usr/bin/env python3
""" returns a tuble from string, int or float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v and is annotated as a float.
    """
    return (k, float(v ** 2))
