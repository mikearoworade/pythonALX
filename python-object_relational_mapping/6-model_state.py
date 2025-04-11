#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Connect to the MySQL server
    # (replace 'username', 'password', and 'database_name' with actual values)
    username = sys.argv[1]  # e.g., 'root'
    password = sys.argv[2]  # e.g., 'admin'
    database = sys.argv[3]  # e.g., 'hbtn_0e_6_usa'

    # Create a connection to the MySQL database
    # engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}') OR
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database), pool_pre_ping=True)

    # Create all tables in the database (this will create the 'states' table)
    Base.metadata.create_all(engine)