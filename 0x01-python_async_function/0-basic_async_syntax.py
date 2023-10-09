#!/usr/bin/env python3
"""
async
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    and eventually returns it.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
