#!/usr/bin/env python3
""" a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay
and returns a asyncio.Task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task object that will execute the wait_random coroutine
    with the given `max_delay` argument.
    """
    return asyncio.create_task(wait_random(max_delay))
