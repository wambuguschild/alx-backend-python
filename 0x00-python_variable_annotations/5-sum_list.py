#!/usr/bin/env python3
"""A function that contains a su of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats
    Args:
        input_list (List[float]): The input list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)
