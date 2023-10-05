#!/usr/bin/env python3
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Takes a sequence and returns its first element if it exists, or None if the sequence is empty.

    :param lst: A sequence of elements of unknown type.
    :return: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
