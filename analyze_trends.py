# analyze_trends.py

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('trends.db')

# Read data into a DataFrame
df = pd.read_sql_query('SELECT * FROM trends', conn)

# Close the connection
conn.close()

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Pivot the data to have dates as index and keywords as columns
df_pivot = df.pivot(index='date', columns='keyword', values='interest')

print("Data Retrieved from Database:")
print(df_pivot.head())

# Plot the trends
plt.figure(figsize=(10, 6))
for kw in kw_list:
    plt.plot(df_pivot.index, df_pivot[kw], label=kw)

plt.title('Google Trends Interest Over Time')
plt.xlabel('Date')
plt.ylabel('Interest')
plt.legend()
plt.tight_layout()
plt.show()
