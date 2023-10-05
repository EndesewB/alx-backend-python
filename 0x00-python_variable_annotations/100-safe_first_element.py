#!/usr/bin/env python3
"""returns first element of the sequence"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Takes a sequence and returns its first element if it exists, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
