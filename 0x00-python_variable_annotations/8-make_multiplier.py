#!/usr/bin/env python3
"""multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the specified multiplier.
        """
        return x * multiplier

    return multiplier_function
