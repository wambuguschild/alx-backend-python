#!/usr/bin/env python3
"""A coroutine that takes no arguments."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ an async generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
