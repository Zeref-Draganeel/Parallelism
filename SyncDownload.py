import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        content=response.content


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.google.com",
        "http://www.youtube.com",
    ] * 30
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
