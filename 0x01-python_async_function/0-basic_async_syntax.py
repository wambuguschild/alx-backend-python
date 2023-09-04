#!/usr/bin/env python3
"""basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """awaits random delay"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
