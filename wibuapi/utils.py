# (c) 2022-2023 Yoga Pranata a.k.a zYxDevs
# This file contains utilities for wibuapi.

import aiohttp


async def getwibu(url: str, timeout: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as response:
            response.raise_for_status()
            return await response.json()
