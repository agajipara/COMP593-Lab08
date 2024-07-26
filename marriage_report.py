import sqlite3
import pandas as pd

# Connect to the social_network database
con = sqlite3.connect('social_network.db')
curs = con.cursor()

# SQL query to get all married couples (relationship type is 'spouse')
married_couples_query = """
SELECT person1.name AS person1_name, person2.name AS person2_name, start_date
FROM relationships
JOIN people person1 ON person1_id = person1.id
JOIN people person2 ON person2_id = person2.id
WHERE type = 'spouse';
"""

# Execute the query and get all results
curs.execute(married_couples_query)
married_couples = curs.fetchall()

# Close the connection
con.close()

# Convert the query results to a pandas DataFrame
married_couples_df = pd.DataFrame(married_couples, columns=['Person 1', 'Person 2', 'Start Date'])

# Generate a CSV file containing names and relationship start date of all married couples
married_couples_df.to_csv('married_couples.csv', index=False)