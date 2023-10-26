#!/usr/bin/env python3

"""
An async comprehension script
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]


if __name__ == '__main__':
    async def main():
        result = await async_comprehension()
        print(result)

    asyncio.run(main())
