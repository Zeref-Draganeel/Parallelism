import _thread as t
import time

import requests


def download_site(url):
    content = requests.get(url).content


def download_all_sites(sites):
    for site in sites:
        t.start_new_thread(download_site, (site,))


if __name__ == "__main__":
    sites = [
                "https://www.google.com",
                "http://www.youtube.com",
            ] * 30
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
