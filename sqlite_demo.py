#!/usr/bin/env python3
"""
sqlite_demo.py - Saving scraped data into SQLite
Creates a table called countries and inserts sample tuples.
"""
import sqlite3

# 1 - Connect (creates file if it doesn’t exist)
conn = sqlite3.connect("data/mydata.db")
cursor = conn.cursor()

# 2 - Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT,
    population TEXT,
    year TEXT,
    population_millions REAL
)
""")

# 3 - Example records (would come from your scraper)
records = [
    ("Canada", "38000000", "2023", 38.0),
    ("India", "1410000000", "2023", 1410.0),
    ("Japan", "125000000", "2023", 125.0)
]

# 4 - Insert each record safely using placeholders

cursor.execute("SELECT COUNT(*) FROM countries")
count = cursor.fetchone()[0]
if (count == 0):
    cursor.executemany(
        "INSERT INTO countries (country, population, year, population_millions) VALUES (?, ?, ?, ?)",
        records
    )

conn.commit()
print("✅ Records inserted successfully!")

# 5 - Verify by reading them back
cursor.execute("SELECT * FROM countries LIMIT 5")
for row in cursor.fetchall():
    print(row)

conn.close()