#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of sequences and returns a list of tuples,
    where each tuple contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
