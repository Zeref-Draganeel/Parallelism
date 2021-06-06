import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        content=response.content


def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.google.com",
        "http://www.youtube.com",
    ] * 30
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
