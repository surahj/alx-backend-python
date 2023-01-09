#!/usr/bin/env python3
""" Measure the runtime """
import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
        Args:
            max_delay: max wait
            n: spawn function
        Return:
            float measure time
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time
