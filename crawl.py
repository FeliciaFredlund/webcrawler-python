"""
Crawl.py
Where the crawl functions live
"""

from urllib.parse import urlsplit

def normalize_url(url: str) -> str:
    split_url = urlsplit(url.strip())
    normalized = split_url.hostname if split_url.hostname != None else ""
    normalized += split_url.path

    return normalized.strip("/")