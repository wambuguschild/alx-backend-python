#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no arguments."""

import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


async def async_comprehension():
    random_numbers = [num async for num in async_generator()]
    return random_numbers
