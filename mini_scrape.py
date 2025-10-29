#!/usr/bin/env python3
"""
mini_scrape.py - Demo of simple web scraping
Collects book categories from https://books.toscrape.com/
"""
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all category links in the sidebar
titles = soup.select("h3 a")

print("Book Categories Found:")
for c in titles:
    name = c.get_text(strip=True)
    link = url + c["href"]
    print(f"- {name}  ({link})")