import asyncio
import time
import aiohttp
import requests

URLS = [
    "https://python.org",
    "https://google.com",
    "https://www.httpbin.org/delay/2",
    "https://github.com",
]

async def check_url(session: aiohttp.ClientSession, url: str):
    print(f'[SZINKRON] lekeres indul: {url}')
    try:
        async with session.get(url) as response:
            print(f'[ASSZINKRON] {url} -> {response.status}')
    except asyncio.TimeoutError as e:
        print(f'[ASSZINKRON] timeout Hiba {url} -> {e}')
    except aiohttp.ClientError as e:
        print(f'[ASSZINKRON] client hiba {url} -> {e}')

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in URLS:
            tasks.append(asyncio.create_task(check_url(session, url)))
        await asyncio.gather(*tasks)

        endTime = time.time()
    print(f'Ossz futtatasi ido (asszinkron): {endTime - start:.2f} mp')

if __name__ == '__main__':
    asyncio.run(main())