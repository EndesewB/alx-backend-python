#!/usr/bin/env python3
from typing import TypeVar, Mapping, Any, Union, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary by key.

    :param dct: A mapping (dictionary) to retrieve the value from.
    :param key: The key to lookup in the dictionary.
    :param default: (optional) The default value to return if the key is not found (default is None).
    :return: The value associated with the key in the dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
