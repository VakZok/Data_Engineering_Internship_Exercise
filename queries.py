import sqlite3

# Connect to the database or create if it doesn't exist
connection = sqlite3.connect("CustomerSales.db")

# Create a cursor
cursor = connection.cursor()

# Execute a query
query = "SELECT * FROM kunde;"
cursor.execute(query)

# Fetch data from the executed query
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and the connection
cursor.close()
connection.close()