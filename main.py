import aiohttp
import asyncio


async def task(url: str, session: aiohttp.ClientSession):
    async with session.get(url) as resp:
        return await resp.json()

async def fetch_all(urls: list[str]) -> list[dict]:
    results = []
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[task(url, session) for url in urls])
        return results

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://jsonplaceholder.typicode.com/todos/2',
        'https://jsonplaceholder.typicode.com/todos/3',
        'https://jsonplaceholder.typicode.com/todos/4',
        'https://jsonplaceholder.typicode.com/todos/5',
        'https://jsonplaceholder.typicode.com/todos/6',
        'https://jsonplaceholder.typicode.com/todos/7',
        'https://jsonplaceholder.typicode.com/todos/8',
        'https://jsonplaceholder.typicode.com/todos/9',
        'https://jsonplaceholder.typicode.com/todos/10',
    ]
    results = await fetch_all(urls)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
