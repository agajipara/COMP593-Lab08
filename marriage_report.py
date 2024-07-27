import sqlite3
import pandas as pd

# Connect to the database
con = sqlite3.connect('social_network.db')  # Replace with your actual database file
curs = con.cursor()

# Execute the SQL query to get a list of all married couples
relationships_table_query = """
SELECT p1.name AS person1_name, p2.name AS person2_name, r.start_date
FROM relationships r
JOIN people p1 ON r.person1_id = p1.id
JOIN people p2 ON r.person2_id = p2.id
WHERE type = 'spouse'
"""

curs.execute(relationships_table_query)

# Fetch all results from the executed query
results = curs.fetchall()

# Define the column names
columns = ['person1_name', 'person2_name', 'start_date']

# Convert the query results to a pandas DataFrame
df = pd.DataFrame(results, columns=columns)

# Generate a CSV file from the DataFrame
df.to_csv('married_couples_report.csv', index=False)

# Close the database connection
con.close()
