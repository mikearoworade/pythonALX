#!/usr/bin/python3
# Displays all cities of a given state from the
# states table of the database hbtn_0e_4_usa.
# Safe from SQL injections.
# Results are sorted in ascending order by cities.id.
# Usage: ./5-filter_cities.py <mysql username> \
#                             <mysql password> \
#                             <database name> \
#                             <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=db_name
    )

    # Create a cursor object to interact with the DB
    cur = db.cursor()

    # SQL query to list all cities for a given state
    query = """
            SELECT cities.id, cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """

    # Execute the query with state_name as a safe parameter
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Display the results
    if rows:
        print(", ".join([row[1] for row in rows]))
    else:
        print()

    # Clean up
    cur.close()
    db.close()
