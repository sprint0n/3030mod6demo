#!/usr/bin/env python3
"""
main.py - Integrating scraper and database
Coordinates the scraping, saving, and verification steps.
"""
import sqlite3
from scraper import scrape_countries
from database import create_table, insert_country
import requests
from bs4 import BeautifulSoup

def main():
    print("Starting scrape...")
    records = scrape_countries()
    print(f"Collected {len(records)} records.")

    print("Saving to database...")
    conn = sqlite3.connect("data/mydata.db")
    create_table(conn)

    insert_country(conn, records)
    
    print("Data saved successfully!")
    conn.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")