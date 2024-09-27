# BirthdayFiller
Authors: Mark Pirella, Adam Shaikh, Sahil Zafar

Change History:
9/27/24:
Added example analyze_trends.py
  Data Retrieval: Connects to the database and reads the trends table into a pandas DataFrame.
  Data Transformation:
  Date Conversion: Converts the date column to datetime objects.
  Pivoting: Reshapes the DataFrame so that each keyword has its own column.
  Data Visualization: Plots the interest over time for each keyword using matplotlib

Added trends_to_sqlite.py
  Initialize PyTrends: Sets up the connection to Google Trends.
  Define Keywords and Timeframe: Specifies the products and time period you're interested in.
  Build Payload and Fetch Data: Retrieves the interest over time for the specified keywords.
  Data Cleanup: Removes any unnecessary columns.
  Database Connection: Connects to (or creates) an SQLite database file named trends.db.
  Table Creation: Creates a table trends with columns for date, keyword, and interest.
  Data Preparation: Transforms the DataFrame into a list of tuples suitable for database insertion.
  Data Insertion: Inserts the records into the database.
  Cleanup: Commits changes and closes the database connection.
