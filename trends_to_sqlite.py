# trends_to_sqlite.py

from pytrends.request import TrendReq
import pandas as pd
import sqlite3

# Initialize PyTrends
pytrends = TrendReq()

# Define the list of keywords and timeframe
kw_list = ["smartphone", "laptop", "tablet"]
timeframe = 'today 3-m'  # Last 3 months

# Build the payload
pytrends.build_payload(kw_list, timeframe=timeframe)

# Get interest over time
data = pytrends.interest_over_time()

# Remove the 'isPartial' column if it exists
if 'isPartial' in data.columns:
    data = data.drop(columns=['isPartial'])

print("Fetched Data:")
print(data.head())

# Connect to SQLite database (creates one if it doesn't exist)
conn = sqlite3.connect('trends.db')
cursor = conn.cursor()

# Create a table to store trends data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trends (
        date TEXT,
        keyword TEXT,
        interest INTEGER
    )
''')

# Prepare data for insertion
data_reset = data.reset_index()
records = []
for index, row in data_reset.iterrows():
    date = row['date'].strftime('%Y-%m-%d')
    for kw in kw_list:
        interest = row[kw]
        records.append((date, kw, int(interest)))

# Insert data into the database
cursor.executemany('INSERT INTO trends (date, keyword, interest) VALUES (?, ?, ?)', records)
conn.commit()

# Close the connection
conn.close()

print("\nData has been stored in the SQLite database 'trends.db'.")

