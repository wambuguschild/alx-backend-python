#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no arguments."""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async generator"""
    results = [i async for i in async_generator()]
    return results
