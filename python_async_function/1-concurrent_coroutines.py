import asyncio
from typing import List
from random import uniform

# Assuming wait_random is defined like this (imported from previous file):
async def wait_random(max_delay: int = 10) -> float:
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Now, define wait_n
async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
