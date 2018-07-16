from time import sleep
import asyncio


# Standard (Synchronous) Python
def hello():
    print('Hello')
    sleep(3)
    print('World')


if __name__ == '__main__':
    hello()


# Asyncio Example1
loop = asyncio.get_event_loop()


@asyncio.coroutine
def hello2():
    print('Hello')
    yield from asyncio.sleep(3)
    print('World!')


if __name__ == '__main__':
    loop.run_until_complete(hello2())

# Asyncio Example2
loop = asyncio.get_event_loop()


@asyncio.coroutine
async def hello2():
    print('Hello')
    await asyncio.sleep(3)
    print('World!')


if __name__ == '__main__':
    loop.run_until_complete(hello2())
