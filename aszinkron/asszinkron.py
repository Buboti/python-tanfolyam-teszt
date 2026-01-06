import random
import time
import asyncio


async def asszinkron(n: int):
    print(f'Szinkron feladat fut {n}')
    sleep_time = random.uniform(0.5, 2.0)
    await asyncio.sleep(sleep_time)
    print(f'Szinkron feladat befejezodott {n} ({sleep_time: .2f})')

async def main():
    start = time.time()
    tasks = []
    for i in range(1, 4):
        tasks.append(asyncio.create_task(asszinkron(i)))

    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f'Ossz futtatasi ido {end_time - start:.2f} mp')

asyncio.run(main())