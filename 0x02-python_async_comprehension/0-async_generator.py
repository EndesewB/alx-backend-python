#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random


async def async_generator():
    """Async Generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    """prints the values that are generated"""
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)
