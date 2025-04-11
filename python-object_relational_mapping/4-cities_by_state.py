#!/usr/bin/python3
# Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
# Usage: ./4-cities_by_state.py <mysql username> \
#                               <mysql password> \
#                               <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=db_name
    )

    # Create a cursor object to interact with the DB
    cur = db.cursor()

    # SQL query to list all cities and sort by id
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """

    # Execute the query and fetch the results
    cur.execute(query)

    [print(city) for city in cur.fetchall()]

    # Clean up
    cur.close()
    db.close()
