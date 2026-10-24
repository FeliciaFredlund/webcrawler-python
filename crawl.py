"""
Crawl.py
Where the crawl functions live
"""

from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

def normalize_url(url: str) -> str:
    split_url = urlsplit(url.strip())

    normalized = split_url.hostname if split_url.hostname != None else ""
    normalized += split_url.path

    return normalized.strip("/")

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    h_tag = soup.h1 if soup.h1 != None else soup.h2
    
    return h_tag.get_text(strip=True) if isinstance(h_tag, Tag) else ""

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    p_tag = soup.main.p if soup.main != None and soup.main.p != None else soup.p

    return p_tag.get_text(strip=True) if isinstance(p_tag, Tag) else ""