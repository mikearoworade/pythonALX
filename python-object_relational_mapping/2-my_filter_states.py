#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    user, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(user=user, passwd=password, db=db_name)

    # Create a cursor object to interact with the DB
    cur = db.cursor()

    # Execute the SQL query using format (not safe from SQL injection)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    [print(state) for state in cur.fetchall()]

    # Clean up
    cur.close()
    db.close()
