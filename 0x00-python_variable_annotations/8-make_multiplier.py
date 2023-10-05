#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that multiplies a float by multiplier.

    :param multiplier: A float to be used for multiplication.
    :return: A function that multiplies a float by the specified multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the specified multiplier.

        :param x: The float to be multiplied.
        :return: The result of the multiplication as a float.
        """
        return x * multiplier

    return multiplier_function
