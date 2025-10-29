#!/usr/bin/env python3
"""
parse_table_demo.py - Example of parsing an HTML table
Reads the first population table from Wikipedia.
"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
response = requests.get(url, headers={"User-Agent": "CS3030-Student"})
soup = BeautifulSoup(response.text, "html.parser")

# Locate the first table with class 'wikitable'
table = soup.find("table", class_="wikitable")

# Extract all rows, skipping the header row
rows = table.find_all("tr")[1:]

print("Sample Output:\n")

for row in rows[:5]:       # only first 5 rows for brevity
    cells = row.find_all("td")
    # Each <td> is a column; convert to text
    values = [c.get_text(strip=True).replace("\xa0", " ") for c in cells]
    print(values[:2])