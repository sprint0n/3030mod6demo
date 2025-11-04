#!/usr/bin/env python3
"""
derived_field_demo.py - Demonstrate creating a derived field
Scrapes a Wikipedia table of countries and calculates population in millions.
"""
import requests
from bs4 import BeautifulSoup


def scrape_countries():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    response = requests.get(url, headers={"User-Agent": "CS3030-Student"})
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", class_="wikitable")
    rows = table.find_all("tr")[1:]

    records = []

    for row in rows[:10]:   # first 10 for readability
        cols = row.find_all("td")
        if len(cols) < 3:
            continue
        country = cols[0].get_text(strip=True)
        population2022 = cols[1].get_text(strip=True).replace(",", "").replace("\xa0", " ")
        population2023 = cols[2].get_text(strip=True).replace(",", "").replace("\xa0", " ")


        # Convert to numeric and compute derived field
        try:
            population_int2022 = int(population2022)
            population_millions2022 = round(population_int2022 / 1_000_000, 2)
            population_int2023 = int(population2023)
            population_millions2023 = round(population_int2023 / 1_000_000, 2)
        except ValueError:
            population_millions = None

        record = (country, population2022, population2023, population_millions2022, population_millions2023)
        records.append(record)
    return(records)
