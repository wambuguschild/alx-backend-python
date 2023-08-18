#!/usr/bin/env python3
"""A function that return values with the appropriate types"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing the element and its length."""
    return [(i, len(i)) for i in lst]
