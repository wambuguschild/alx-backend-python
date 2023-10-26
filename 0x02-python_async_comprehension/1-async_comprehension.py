#!/usr/bin/env python3
"""
Module imports the async generator function and defines a corouting called
async_comprehension that takes no arguments.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine creates a list of 10 numbers from a 10-number generator.
    """
    return [rand async for rand in async_generator()]
