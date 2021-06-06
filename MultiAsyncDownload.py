'''
Failed idea
'''
import asyncio
import concurrent.futures
import multiprocessing
import threading
import time

import aiohttp
import requests

thread_local = threading.local()
session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


async def download_site(session, url):
    async with session.get(url) as response:
        content = response.content


async def download_all_sites(sites):
    with multiprocessing.Pool(initializer = set_global_session) as pool:
        with concurrent.futures.ThreadPoolExecutor(max_workers = 1000) as executor:
            async with aiohttp.ClientSession() as session:
                tasks = []
                for url in sites:
                    task = asyncio.ensure_future(download_site(session, url))
                    tasks.append(task)
                await asyncio.gather(*tasks, return_exceptions = True)


if __name__ == "__main__":
    sites = [
        "https://www.india.gov.in",
        "http://www.google.com",
    ] * 30
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
