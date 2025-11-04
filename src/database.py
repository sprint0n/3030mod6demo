#!/usr/bin/env python3
"""
sqlite_demo.py - Saving scraped data into SQLite
Creates a table called countries and inserts sample tuples.
"""
import sqlite3

# 1 - Connect (creates file if it doesn’t exist)
conn = sqlite3.connect("data/mydata.db")
cursor = conn.cursor()
def create_table(conn):
# 2 - Create the table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT,
        population_2022 TEXT,
        popluation_2023 TEXT,
        population_millions_2022 REAL,
        population_millions_2023 REAL
    )
    """)
    conn.commit()



# 3 - Example records (would come from your scraper)


# 4 - Insert each record safely using placeholders
def insert_country(conn, records):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM countries")
    count = cursor.fetchone()[0]
    if (count == 0):
        cursor.executemany(
            "INSERT INTO countries (country, population_2022, popluation_2023, population_millions_2022, population_millions_2023) VALUES (?, ?, ?, ?, ?)",
        records 
    )

    conn.commit()
    print("✅ Records inserted successfully!")

