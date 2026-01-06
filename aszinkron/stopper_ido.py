import asyncio
import time


async def stopper():
    start = time.time()
    while True:
        elapsed = time.time() - start
        print(f'Eltelt ido: {elapsed:.1f} msp')
        await asyncio.sleep(1.0)

async def short_task():
    print('Rovid kis feladat')
    await asyncio.sleep(2)
    print('Rovid feladat vege 2 mp')

async def long_task():
    print('Hosszu feladat')
    await asyncio.sleep(9)
    print('Hosszu feladat vege 9 mp')

async def main():
    stopper_task = asyncio.create_task(stopper())
    short_t= asyncio.create_task(short_task())
    long_t = asyncio.create_task(long_task())

    await asyncio.gather(short_t, long_t)

    stopper_task.cancel()

asyncio.run(main())